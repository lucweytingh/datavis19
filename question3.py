from init import *
import math
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
from bokeh.models import Range1d
import numpy
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

def add_to_plot_undernourish(plot, name, dates, values):
    return plot.line(datetimeyear(dates), values, color='#'+"%06x" % random.randint(0, 0xFFFFFF))

def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)


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

def plotter(country, item = None):
    if item == None:
        products = pd_data.filter({'country_name':country})['item_name'].unique()
    else:
        products = [item]
    plot1 = figure(x_axis_type="datetime", title= 'Food Price'+ country)
    legend = []
    for item in products:
        itemdata = listconverter(nodata_filter(food_data(country,item)),0)
        sorteddates = sort_dates(itemdata)
        print(item)
        dates , data = split_date_and_values(sorteddates)
        legend.append((item,[add_to_plot(plot1,item +' ' + country,dates,data)]))
    plot(plot1,legend) 

def checkEqual2(iterator):
   return len(set(iterator)) <= 1


def coeff(country,limit):
    products = pd_data.filter({'country_name':country})['item_name'].unique()
    coeffs = {}
    counter = 0
    for item in products:
        itemdata = listconverter(nodata_filter(food_data(country,item)),0)
        noudata = listconverter(nodata_filter(food_data(country,item)),1)
        dates, itemdata = split_date_and_values(itemdata)
        dates, noudata  = split_date_and_values(noudata)
        itemdata = list(map(float,itemdata))
        noudata = list(map(float,noudata))
        if checkEqual2(noudata):
            coeffs[item] = 0
        
        elif len(itemdata) > limit:
            counter += 1
            coeffs[item] = np.corrcoef(itemdata,noudata)[0][1]
    #print(counter)
    return counter, coeffs
    

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

print(coeff('Afghanistan', 60))

def produce_result(country,limit,item = None):
    coeff(country,limit)
    plotter(country, item)
    undernourishmentplotter(country)


def biggestcorrelator(limit):    
    countries = pd_data['country_name'].unique()
    res = []
    fcounter = 0
    zerocounter = 0
    for country in countries:
        print(country)     
        if country == 'Myanmar':
            continue   
        counter, countrydict = coeff(country,limit)
        fcounter += counter
        if counter == 0:
            zerocounter += 1
        for key, value in countrydict.items():
            res.append(((country,key),value))
    
    longenough = fcounter/len(countries)


    sortedlist = sorted(res,key=lambda x: x[1], reverse=True)
    
    cum = {}
    for instance in sortedlist:
        if instance[0][1] in cum.keys():
            cum[instance[0][1]].append(instance[1])
        else:
            cum[instance[0][1]] = [instance[1]]
    cumulative = []
    for key, value in cum.items():
        ans = numpy.count_nonzero(~np.isnan(value))
        cumulative.append((key,numpy.nansum(value)/(ans)))
    sortedcumulative = sorted(cumulative,key=lambda x: x[1], reverse=True)
    print(sortedcumulative)



    # for i in range(10):
    #     obj = ten[i]
    #     print('Correlation ' + str(i + 1) + ' is ' + str(obj[0][1]) + ' in ' + str(obj[0][0]) + ' with R ' + str(obj[1]))
    # for product in sortedlist[:10]:
    #     plotter(product[0][0],product[0][1])  
    #     undernourishmentplotter(product[0][0])
           
    #     dnext = input('continue?: ')  


#biggestcorrelator(60)

def undernourishmentdict(country):
    data = pd_data.filter({'country_name' : country})
    result = {}
    for index, row in data.iterrows():
        if row['undernourishment'] != 'No Data':
            result[(row['month'],row["year"])] = row['undernourishment']
    return result

def getundernourishment(country):
    result = []
    country = und_data.filter({"Entity":country})
    for index,row in country.iterrows():
        result.append((row['Year'],row['POU']))
    return result

def regionundernourishment():
    plot1 = figure(x_axis_type="datetime", title='region undernourishment')
    legend = []
    regions = und_data["region"].unique()
    for region in regions:
        if region == "No Data":
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
        legend.append((regionname,[add_to_plot_undernourish(plot1, regionname,dates,data)]))
    plotundernourishment(plot1,legend)

#regionundernourishment()


def avg_items():
    countries = pd_data["country_name"].unique()
    totprods = 0
    for country in countries:
        country_data = pd_data.filter({'country_name': country})
        print(country_data['item_name'].unique())
        productsnum = len(country_data['item_name'].unique())
        
        totprods += productsnum
    return totprods/len(countries)
