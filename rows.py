from init import *
import math
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d
import numpy

rowcount = []
rowsum = 0
dates = []

for year, data in pd_data.split('year').items():
  for month, month_data in data.split('month').items():
    rowsum += month_data.shape[0]
    rowcount.append(rowsum)
    dates.append((month, year))

def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)

def plot(plot, legend_names):
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Aantal rijen'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')

    show(gridplot([[plot]], plot_width=1000, plot_height=600))  # open a browser

def add_zero(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)

def add_to_plot(plot, name, dates, values):
    return plot.line(datetime(dates), values, color='#1982C4')

plot1 = figure(x_axis_type="datetime", title='Cumulatieve rijen door de jaren heen')
legend = []
# legend.append(('Aantal',[add_to_plot(plot1,'rowcount',dates,rowcount)]))
add_to_plot(plot1,'rowcount',dates,rowcount)
plot(plot1,legend)