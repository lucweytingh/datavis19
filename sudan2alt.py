from init import *
import math
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d
import numpy


# {"country_name": "Tajikistan", "market_id": 303, "item1": "Lamb", "item2": "Beef", "correlation": 0.9990224502367437}

market = pd_data.filter({ 'country_name': 'South Sudan', 'market_name': 'Bor', 'year': ['2015', '2016', '2017', '2018'] }).dict_from_columns(['market_name', 'item_name'], ['price', 'date'])

def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)

def plot(plot, legend_names):
    plot.toolbar.logo = None
    plot.toolbar_location = None
    plot.title.text_color = "white"
    plot.background_fill_alpha = 0
    plot.border_fill_alpha = 0
    plot.grid.grid_line_color='white'
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Datum'
    plot.xaxis.axis_label_text_color = 'white'
    plot.xaxis.axis_line_color = "white"
    plot.xaxis.major_label_text_color = "white"
    plot.yaxis.axis_label = 'Prijs (lokale munteenheid)'
    plot.yaxis.axis_line_color = "white"
    plot.yaxis.major_label_text_color = "white"
    plot.yaxis.axis_label_text_color = 'white'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')

    show(gridplot([[plot]], sizing_mode='stretch_both'))  # open a browser

def add_zero(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)

colors = ['#e125e8', '#8a9dcd', '#c1bfec', '#afa5e2', '#f675f8', '#d48962', '#d14625', '#7e0dd6', '#43d852', '#43a4d8', '#7a28f6', '#971267', '#e036b1', '#7cc962', '#1829ca', '#31c63b', '#c85172', '#e366ec', '#5e5b46', '#f2ea12']
i = 0

def add_to_plot(plot, name, dates, values):
  return plot.line(dates, values, color=colors[i], line_width=2)

plot1 = figure(x_axis_type="datetime", title='Bor, Zuid Soedan', sizing_mode='stretch_both')
legend = []

for item, data in market['Bor'].items():
  add_to_plot(plot1,item,data['date'],data['price'])
  i += 1
plot(plot1,legend)
