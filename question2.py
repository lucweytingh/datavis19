from compare_regions import *
import simplejson
import math

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

from plot import *


# in this question we are trying to anwser if countries in similar regions also show similar price differences

def main():
  # to awnser this we find the top correlating countries for certain items and see if they are in the same region
  # correlation([0], pd_data['item_name'].unique(), 10)

  items = pd_data['item_name'].unique()
  compare_to_global(items, 0.4)
  


def compare_to_global(items, corrcoef):
    # normally, global_data = gather_data([1,2,3,4,5,6], items)
    # but for efficiency purposes, global_data is saved in a file

    file1 = open("data/global_data.txt")
    global_data = simplejson.load(file1)
    item_amount = len(items)
    points_for_regions = 0
    points_for_global = 0

    regions = pd_data['region_name'].unique()
    
    region_results = {}
    region_total = {}
    for region in regions:
      region_results[region] = 0
      region_total[region] = 0

    # result_file = open("question2_regional_results.txt", 'w')
    for item_data in global_data:
        highest, lowest = find_top_corr([item_data], None)
        for i in range(len(highest)):
          # result_file.write(highest[i][0][0] + ';' +highest[i][1][0] + ';' + str(highest[i][1][1])+'\n')
          value = highest[i][1][1]
          region_total[highest[i][0][1]] += 1
          region_results[highest[i][0][1]] += value
            

    for region in regions:
      print(region + ': r=' + str(region_results[region] / region_total[region]))
    

    bar_plot('Average correlation between countries per product', "r", regions, [region_results[region] / region_total[region] for region in regions])


def bar_plot(plot_name, y_axis_name, bar_names, bar_values):
  
  output_file('charts/' + plot_name.replace(" ", "_").lower() + ".html")

  source = ColumnDataSource(data=dict(bar_names=bar_names, bar_values=bar_values))

  p = figure(x_range=bar_names, plot_height=400, plot_width=600, title=plot_name)
  p.vbar(x='bar_names', top='bar_values', width=0.9, source=source,
        line_color='white', fill_color=factor_cmap('bar_names', palette=Spectral6, factors=bar_names))

  p.xgrid.grid_line_color = None
  p.y_range.start = 0
  p.y_range.end = max(bar_values) * 1.2
  p.legend.orientation = "horizontal"
  p.legend.location = "top_center"
  p.yaxis.axis_label = y_axis_name
  p.xaxis.major_label_orientation = math.pi/4

  show(p)


if __name__ == "__main__":
  main()



