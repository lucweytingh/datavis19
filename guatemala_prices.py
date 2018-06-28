from init import *
import math
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d
import numpy
from compare_regions import *
dic_id_name = {1: "South Asia", 2:"Middle East & North Africa", 3:"Europe & Central Asia",
            4:"Sub-Saharan Africa", 5:"Latin America & Caribbean", 6:"East Asia & Pacific"}

def isNaN(num):
    return num != num

def food_data(country, item):
    food_data = {}
    data = pd_data.filter({'country_name':country, 'item_name':item})
    for index, row in data.iterrows():
        date = (row["month"],row["year"])
        if date in food_data.keys():
            food_data[date][0].append(row['price'])
        else:
            food_data[date] = [[row['price']],row['undernourishment']]
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
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Datum'
    plot.yaxis.axis_label = 'Ondervoedingsindex'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')

    show(gridplot([[plot]], sizing_mode='stretch_both'))  # open a browser

def add_to_plot(plot,name, dates, values):
    return plot.line(datetime(dates), values, line_width = 2,color='#'+"%06x" % random.randint(0, 0xFFFFFF))

def add_to_plot_undernourish(plot, name, dates, values, color):
    return plot.line(datetimeyear(dates), values, line_width = 2, color=color)


def datetimeyear(dates):
    format = [str(x)+'-'+'01'+'-01' for x in dates]
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

def country_product_plotter(country, item = None):
    if item == None:
        products = pd_data.filter({'country_name':country})['item_name'].unique()
    else:
        products = [item]
    plot1 = figure(x_axis_type="datetime", title= 'Product Price '+ country)
    legend = []
    for item in products:
        itemdata = listconverter(nodata_filter(food_data(country,item)),0)
        sorteddates = sort_dates(itemdata)
        print(item)
        dates , data = split_date_and_values(sorteddates)
        legend.append((item,[add_to_plot(plot1,item +' ' + country,dates,data)]))
    plot(plot1,legend)

# country_product_plotter("Guatemala")

def checkEqual2(iterator):
   return len(set(iterator)) <=  1


def coeff_country_undernourish(country,limit):
    products = pd_data.filter({'country_name':country})['item_name'].unique()
    coeffs = {}
    counter = 0
    for item in products:
        data = nodata_filter(food_data(country,item))
        itemdata = listconverter(data,0)

        noudata = listconverter(data,1)
        dates, itemdata = split_date_and_values(itemdata)
        dates, noudata  = split_date_and_values(noudata)
        itemdata = list(map(float,itemdata))
        noudata = list(map(float,noudata))
        if checkEqual2(noudata):
            coeffs[item] = 0
        elif len(itemdata) > limit:
            counter += 1
            coeffs[item] = np.corrcoef(itemdata,noudata)[0][1]
    return counter, coeffs


# print(coeff_country_undernourish('Afghanistan', 0))

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

def undernourishmentplotteryear(country):
    plot1 = figure(x_axis_type="datetime", title=country + 'undernourishment')
    legend = []
    data = undernourishmentlist(country)
    sorteddata = sort_dates(data)
    dates , data = split_date_and_values(sorteddata)
    legend.append(('name',[add_to_plot_undernourish(plot1,'name',dates,data)]))
    plotundernourishment(plot1,legend)


def biggestcorrelator(limit):
    countries = pd_data['country_name'].unique()
    res = []
    fcounter = 0
    zerocounter = 0
    print(len(countries))
    for country in countries:
        print(country)
        if country == 'Myanmar':
            continue
        counter, countrydict = coeff_country_undernourish(country,limit)
        fcounter += counter
        if counter == 0:
            zerocounter += 1
        for key, value in countrydict.items():
            res.append(((country,key),value))

    longenough = fcounter/len(countries)


    sortedlist = sorted(res,key=lambda x: x[1], reverse=True)

    ten = sortedlist[:10]
    for i in range(10):
        obj = ten[i]
        print("<tr><td>" + str(obj[0][1]) + '</td><td>' + str(obj[0][0]) + '</td><td>' + str(obj[1]) + "</td></tr>")




def avgundernourishment(corrlist):
    cum = {}
    for corr in corrlist:
        if corr[0][1] in cum.keys():
            cum[corr[0][1]].append(corr[1])
        else:
            cum[corr[0][1]] = [corr[1]]
    print(cum)

    cumulative = []
    for key, value in cum.items():
        ans = numpy.count_nonzero(~np.isnan(value))
        cumulative.append((key,numpy.nansum(value)/(ans)))

    sortedcumulative = sorted(cumulative,key=lambda x: x[1], reverse=False)

    ten = sortedcumulative[:10]
    for i in range(10):
        obj = ten[i]
        print(str(obj[0]) + ',' + str(obj[1]))

# avgundernourishment(biggestcorrelator(60))




def getundernourishment(country):
    result = []
    country = und_data.filter({"Entity":country})
    for index,row in country.iterrows():
        result.append((row['Year'],row['POU']))
    return result

def regionundernourishment():
    plot1 = figure(x_axis_type="datetime", title='Ondervoedingsindex per regio', sizing_mode='stretch_both')
    legend = []
    regions = und_data["region"].unique()
    colors = ['#511f8d', '#7eae2b', '#f308cf', '#7a0506', '#6a11cd', '#dfb3b4', '#c2531b', '#3683d0', '#43d7b1', '#c8bf13', '#2afa23', '#60a577', '#aad31d', '#09bdcd', '#d5fdad', '#1ea4a8', '#a7726d', '#4aecb5', '#7d0963', '#2f3d5a']
    i = 0
    for region in regions:
        print(region)
        if region == "No Data" or region == "No Datastates    ":
            continue
        #print(region)
        countries = und_data.filter({'region': region})["Entity"].unique()
        regionundernourishment = []
        for country in countries:
            country = getundernourishment(country)
            regionundernourishment.extend(country)
        avgregion = {}
        for stat in regionundernourishment:
            if stat[0] not in avgregion:
                avgregion[stat[0]] = [stat[1]]
            if stat[0] in avgregion:
                avgregion[stat[0]].append(stat[1])
        for key, value in avgregion.items():
             avgregion[key] = sum(list(map(float,value)))/ len(list(map(float,value)))
        regionname = dic_id_name[int(region)]
        sorteddata = sorted(list(avgregion.items()), key=lambda x: x[0])
        dates , data = split_date_and_values(sorteddata)
        legend.append((regionname,[add_to_plot_undernourish(plot1, regionname,dates,data, colors[i])]))
        i += 1
    plotundernourishment(plot1,legend)

country_product_plotter("Guatemala")
