from init import *
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d


def food_data(country, item):
    food_data = {}
    data = pd_data.filter({'country_name':country, 'item_name':item})
    for index, row in data.iterrows():
        date = (row["month"],row["year"])
        if date in food_data.keys():
            
            food_data[date][0].append(row['price_usd'])
        else:
            food_data[date] = [[row['price_usd']],row['undernourishment']]
    for key, value in food_data.items():
        food_data[key][0] = sum(food_data[key][0])/ len(food_data[key][0])
    return food_data


def nodata_filter(data):
    newdata = {}
    for key,value in data.items():
        if value[1] != 'No Data' :
            newdata[key] = value
    return newdata



# index is a tuple with your first index and second index of what you want to make a list of


def plot(plot, legend_names):
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Price (usd)'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')
    show(gridplot([[plot]], plot_width=1000, plot_height=600))  # open a browser


def plotundernourishment(plot, legend_names):
    plot.y_range = Range1d(0, 100)
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Undernourishment index'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')
    show(gridplot([[plot]], plot_width=1000, plot_height=600))  # open a browser

def add_to_plot(plot, name, dates, values):
    return plot.line(datetime(dates), values, color='#'+"%06x" % random.randint(0, 0xFFFFFF))

def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)

def add_zero(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)

def get_most_product(country):
   products = pd_data.filter({'country_name':country})['item_name'].unique()
   for item in products:
        print("the coeff of "+ item + " is")
        print(coeffmaker(country, item))

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

def listconverter(dict1,index):
    outp = []
    for keys,values in dict1.items():
        outp.append((keys,(values[index])))
    return outp

def split_date_and_values(both):
    return [x[0] for x in both], [x[1] for x in both]

def plotter(country):
    products = pd_data.filter({'country_name':country})['item_name'].unique()
    plot1 = figure(x_axis_type="datetime", title= 'Food Price')
    legend = []
    for item in products:
        itemdata = listconverter(nodata_filter(food_data(country,item)),0)
        sorteddates = sort_dates(itemdata)
        print(item)
        dates , data = split_date_and_values(sorteddates)
        legend.append((item,[add_to_plot(plot1,item,dates,data)]))
    plot(plot1,legend)

def checkEqual2(iterator):
   return len(set(iterator)) <= 1


def coeff(country):
    products = pd_data.filter({'country_name':country})['item_name'].unique()
    coeffs = {}
    for item in products:
        itemdata = listconverter(nodata_filter(food_data(country,item)),0)
        noudata = listconverter(nodata_filter(food_data(country,item)),1)
        dates, itemdata = split_date_and_values(itemdata)
        dates, noudata  = split_date_and_values(noudata)
        itemdata = list(map(float,itemdata))
        noudata = list(map(float,noudata))
        if checkEqual2(noudata):
            coeffs[item] = 0
        else:
            coeffs[item] = np.corrcoef(itemdata,noudata)[0][1]
    return coeffs
    

def undernourishmentlist(country):
    data = pd_data.filter({'country_name' : country})
    result = []
    for index, row in data.iterrows():
        if row['undernourishment'] != 'No Data':
            result.append(((row['month'],row["year"]),row['undernourishment']))
    return list(set(result))

def undernourishmentplotter(country):
    plot1 = figure(x_axis_type="datetime", title=country + 'undernourishment')
    legend = []
    data = undernourishmentlist(country)
    sorteddata = sort_dates(data)
    dates , data = split_date_and_values(sorteddata)
    legend.append(('name',[add_to_plot(plot1,'name',dates,data)]))
    plotundernourishment(plot1,legend)

def produce_result(country):
    coeff(country)
    plotter(country)
    undernourishmentplotter(country)


#produce_result('Ghana')


def biggestcorrelator():
    countries = pd_data['country_name'].unique()
    res = []
    for country in countries:
        print(country)
        countrydict = coeff(country)
        for key, value in countrydict.items():
            res.append(((country,key),value))

    sortedlist = sorted(res,key=lambda x: x[1], reverse=True)
    ten = sortedlist[:10]
    for i in range(10):
        obj = ten[i]
        print('Correlation ' + str(i) + ' is ' + str(obj[0][1]) + ' in ' + str(obj[0][0]) + ' with R ' + str(obj[1]))

print(biggestcorrelator())


