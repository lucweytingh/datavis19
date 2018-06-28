from init import *
import math
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d
import numpy


# {"country_name": "Tajikistan", "market_id": 303, "item1": "Lamb", "item2": "Beef", "correlation": 0.9990224502367437}

market = pd_data.filter({ 'country_name': 'Ukraine', 'market_name': 'National Average', 'item_name': ['Milk', 'Sour cream', 'Curd', 'Butter']}).dict_from_columns(['market_name', 'item_name'], ['price_usd', 'date'])

print(market)

def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)

def plot(plot, legend_names):
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Datum'
    plot.yaxis.axis_label = 'Prijs (USD)'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')

    show(gridplot([[plot]], sizing_mode='stretch_both'))  # open a browser

def add_zero(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)

colors = ['#1982C4', '#37C656', '#FFC014', '#D6262F']
i = 0

def add_to_plot(plot, name, dates, values):
  return plot.line(dates, values, color=colors[i], line_width=2)

plot1 = figure(x_axis_type="datetime", title='Prijs van Milk, Sour cream, Curd en Butter in Oekraïne', sizing_mode='stretch_both')
legend = []
# legend.append(('Aantal',[add_to_plot(plot1,'rowcount',dates,rowcount)]))

for item, data in market['National Average'].items():
  legend.append((item,[add_to_plot(plot1,item,data['date'],data['price_usd'])]))
  i += 1
plot(plot1,legend)
