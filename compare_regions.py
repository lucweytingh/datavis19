from init import *


def main():
    data, item = compare(6)
    plot1 = figure(x_axis_type="datetime", title="Average food price of " + item.lower())
    legend = []
    for name in data:
        date_values = sort_dates(data[name])
        dates, values = split_date_and_values(date_values)
        legend.append((name, [add_to_plot(plot1, name, dates, values)]))
    plot(plot1, legend)

def add_to_plot(plot, name, dates, values):
    return plot.line(datetime(dates), values, color='#'+"%06x" % random.randint(0, 0xFFFFFF))

def plot(plot, legend_names):
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Price (usd)'
    legend = Legend(items=legend_names, location=(0, -30))
    plot.add_layout(legend, 'right')

    show(gridplot([[plot]], plot_width=1000, plot_height=600))  # open a browser

# add a zero before number if needed
def add_zero(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)

# split the date and values in two separate lists
def split_date_and_values(both):
    return [x[0] for x in both], [x[1] for x in both]

# input list of dates in tuple format (mm-yyyy), return datetime array
def datetime(dates):
    format = [str(x[1])+'-'+add_zero(x[0])+'-01' for x in dates]
    return np.array(format, dtype=np.datetime64)

# sort a list of dates (+ values) in tuple format (mm-yyyy) in chronological order
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


# finds the most common item in a region or overall
def most_common_item(region_id=None):
    if region_id == None:
        region = pd_data
    else:
        region = pd_data.filter({'region_id':region_id})
    options = region['item_name'].unique()
    result_count = 0
    result_item = ""
    for item in options:
        attempt = len(region.filter({'item_name':item})['country_name'].unique())
        if attempt > result_count:
            result_count = attempt
            result_item = item
    return result_item


# compares regions
def compare(region_id = None, item = None):
    all_dic = {}
    if item == None:
        item = most_common_item(region_id)
    if region_id == None:
        evaluate_name= 'region_name'
        unique = pd_data[evaluate_name].unique()
    else:
        evaluate_name = 'country_name'
        unique = pd_data.filter({'region_id':region_id})[evaluate_name].unique()
    for data_item in unique:
        data = pd_data.filter({evaluate_name:data_item})
        data_dic = {}
        for index, row in data.filter({'item_name':item}).iterrows():
            if (row['month'], row['year']) not in data_dic:
                data_dic[(row['month'], row['year'])] = [row['price_usd']]
            else:
                data_dic[(row['month'], row['year'])].append(row['price_usd'])
        average = []
        for month, year in data_dic:
            average.append(((month, year), sum(data_dic[(month,year)]) / len(data_dic[(month,year)])))
        all_dic[data_item] = average
    return all_dic, item


if __name__ == "__main__":
    from bokeh.layouts import gridplot
    from bokeh.plotting import figure, show, output_file
    from bokeh.models import Legend
    # test_dates = [((1, 2006), 0.2768810516701759), ((2, 2006), 0.28593047558787704), ((3, 2006), 0.28802077470255943), ((4, 2006), 0.28738613596635715), ((5, 2006), 0.2860767156720411), ((6, 2006), 0.29261475828304473), ((7, 2006), 0.27963102968064624), ((11, 2006), 0.32396098841041737), ((1, 2004), 0.2527255874820858), ((2, 2004), 0.2596318750083353), ((3, 2004), 0.2576683009971368), ((4, 2004), 0.2674213554900618), ((5, 2004), 0.25713157618574906), ((6, 2004), 0.25772099841343993), ((7, 2004), 0.2580106042676619), ((8, 2004), 0.2551941803997591), ((9, 2004), 0.2589134990052946), ((10, 2004), 0.2597369740466546), ((11, 2004), 0.28608626565652484), ((12, 2004), 0.27836322846993933), ((1, 2005), 0.26436998595299055)]
    # test_dates = sort_dates(test_dates)
    # dates, values = split_date_and_values(test_dates)
    # print(dates)
    # main()