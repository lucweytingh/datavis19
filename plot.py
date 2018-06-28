from init import *
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


def plot_data(data, columns, axes = None, title_appendix = None, blacklist = []):
  results = data.dict_from_columns(columns, axes, blacklist)
  for country, markets in results.items():
    for market, items in markets.items():
      plt.clf()
      for item, dic in items.items():
        if title_appendix == None:
          title = "{0}, {1}".format(country, market)
        else:
          title = "{0}, {1} - {2}".format(country, market, title_appendix)
        plt.title(title)
        plt.plot(dic["date"], dic["price"], label=item)
      plt.xlabel('Date')
      plt.ylabel('Price (USD)')
      plt.legend(loc='upper left')
      plt.show()

def plot_by_item(data, title_appendix = None, blacklist = []):
  plot_data(data, ['country_name', 'item_name', 'market_name'], None, title_appendix, blacklist)

def plot_by_market(data, title_appendix = None, blacklist = []):
  plot_data(data, ['country_name', 'market_name', 'item_name'], None, title_appendix, blacklist)


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
