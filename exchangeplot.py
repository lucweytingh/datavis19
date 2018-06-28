from init import *
import math
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d
import numpy


def currency_list_maker(ex_data, currency, dates, stattype = "Average of observations through period"):
    tuples = []
    months = ex_data.filter({'CURRENCY': currency, "Collection": stattype, 'Frequency': 'Monthly'})

    for date in dates:
      tuples.append((totuple_format(date), months[date].unique()[0]))
    return tuples

def totuple_format(form):
  return (int(form[5:]), int(form[:4]))


def datemaker(pd_data, country):
    months = pd_data.filter({'country_name':country})['month'].tolist()
    years = pd_data.filter({'country_name':country})['year'].tolist()
    return list(zip(months,years))

def to_exchange_format(list):
    exchangeform = []
    for tuple in list:
        if len(str(tuple[0])) != 1:
            exchangeform.append(str(tuple[1])+'-'+str(tuple[0]))
        else:
            exchangeform.append(str(tuple[1])+'-0'+str(tuple[0]))
    return exchangeform


def add_to_plot(plot, name, dates, values):
    return plot.line(datetime(dates), values, color='#1982C4', line_width=2)

def plot(plot, legend_names):
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Datum'
    plot.yaxis.axis_label = 'Koers MMK/USD'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')

    show(gridplot([[plot]], sizing_mode='stretch_both'))  # open a browser

def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)

def add_zero(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)

def split_date_and_values(both):
    return [x[0] for x in both], [x[1] for x in both]

def sort_dates(dates):
    if dates == []: return []
    else:
        result = [dates[0]]
        del(dates[0])
        while dates != []:
            for i in range(len(result)):
                if dates[0][0][1] < result[i][0][1]:
                    result.insert(i, dates[0])
                    del(dates[0])
                    break
                elif dates[0][0][1] == result[i][0][1]:
                    if dates[0][0][0] < result[i][0][0]:
                        result.insert(i, dates[0])
                        del(dates[0])
                        break
                if i == len(result) - 1:
                    result.append(dates[0])
                    del(dates[0])
        return result

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


plot1 = figure(x_axis_type="datetime", title= 'Wisselkoers Burmese kyat (MMK/USD)', sizing_mode='stretch_both')
legend = []
dates = datemaker(pd_data, 'Myanmar')
datesexc = to_exchange_format(dates)
data = f7(currency_list_maker(ex_data,'MMK',datesexc))
data = sort_dates(data)

dates, data2 = split_date_and_values(data)

legend.append(('MMK',[add_to_plot(plot1,'Myanmar MMK',dates,data2)]))
plot(plot1,legend)

