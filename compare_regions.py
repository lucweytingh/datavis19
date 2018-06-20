from init import *
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend

# regions
# 0: the world, 1: South Asia, 2: Middle East & North Africa,
# 3: Europe & Central Asia, 4: Sub-Saharan Africa,
# 5: Latin America & Caribbean, 6: East Asia & Pacific

def main_plot(): 
    data, item, region = compare(None, None)
    plot1 = figure(x_axis_type="datetime", title="Average food price of " + item.lower() + ' in ' + region)
    legend = []
    for name in data:
        if data[name] != []:
            dates, values = split_date_and_values(data[name])
            legend.append((name, [add_to_plot(plot1, name, dates, values)]))
    if len(legend) > 1:
        plot(plot1, legend)

def main_correlation():
    interesting_items = ['Petrol', 'Sugar', 'Oil (sunflower)', 'Wheat', 'Beans', 'Tomatoes'] # all: pd_data['item_name'].unique()
    regions = [None, 1, 2, 3, 4, 5, 6]
    correlation(regions, interesting_items, 4)

# plot the top given amount of pos & neg correlations of given items in given regions
def correlation(regions, items, amount):
    data_sets = []
    print("")
    print("Gathering data..")
    for i in regions:
        if i == None:
            message = "all regions"
        elif i == 0:
            message = 'all countries'
        else: 
            message = pd_data.filter({'region_id':i})['region_name'].unique()[0]
        print("     for " + message + '..')
        for item in items:
            print("         about " + item + '..')
            data, item, region = compare(i, item)
            data_sets.append([data, item, region])

    print("")
    print("Finding top correlation..")
    top_corr_high, top_corr_low = find_top_corr(data_sets, amount)
    plot_results(data_sets, top_corr_high + top_corr_low)

def plot_results(data_sets, corr_list):
    for corr in corr_list:
        data = find_data_set(corr[0], data_sets)
        plot1 = figure(x_axis_type="datetime", title="Average food price of " + corr[0][0].lower() + ' in ' + corr[0][1] + ':' + ' a correlation of ' + str(corr[1][1]))
        legend = []
        colors = ['#e6194b', '#0082c8']
        count = 0
        for name in data:
            if name in corr[1][0]:
                if data[name] != []:
                    dates, values = split_date_and_values(data[name])
                    if corr[0][1] == 'all countries of the world':
                        region = pd_data.filter({'country_name':name})['region_name'].unique()[0]
                        legend.append((name + ' (' + region + ')', [add_to_plot(plot1, name, dates, values, colors[count])]))
                    else:    
                        legend.append((name, [add_to_plot(plot1, name, dates, values, colors[count])]))
                    count += 1
        plot(plot1, legend)

def find_data_set(input, data_sets):
    item, region = input[0], input[1]
    for [data_set, item_name, region_name] in data_sets:
        if item_name == item and region_name == region:
            return data_set

def n_correlations(n_lines):
    if n_lines == 2:
        return 1
    if n_lines == 1:
        return 0
    if n_lines < 1:
        return 0
    return n_lines - 1 + n_correlations(n_lines-1)

def insert_if_hilow(win_list, input_list, item_name, region_name, max_length):
    if max_length > len(win_list):
        min = 0
    else:
        min = len(win_list) - max_length
    if input_list == []:
        return win_list[:max_length], win_list[min:][::-1]
    if win_list == []:
        win_list = [((item_name, region_name), input_list[0])]
        del(input_list[0])
    while input_list != []:
        for i in range(len(win_list)):
            if input_list[0][1] > win_list[i][1][1]:
                win_list.insert(i, ((item_name, region_name), input_list[0]))
                del(input_list[0])
                break
            if i == len(win_list) - 1:
                win_list.append(((item_name, region_name), input_list[0]))
                del(input_list[0])
                break
    return win_list[:max_length], win_list[min:][::-1]


# return the  
def find_top_corr(data_sets, amount):
    max_amount = len(data_sets)
    if amount > max_amount:
        amount = max_amount
    result_high, result_low = [], []
    for data_set in data_sets:
        corr_list = calc_corr(data_set[0])
        result_high, result_low = insert_if_hilow(result_high + result_low[::-1], corr_list, data_set[1], data_set[2], amount)
    return result_high, result_low

def calc_corr(data_set):
    data_set = list(data_set.items())
    results = []
    for i in range(len(data_set)):
        for j in range(i+1, len(data_set)):
            # find datasets in common
            data1, data2 = data_in_common(data_set[i][1], data_set[j][1])
            # append names and corrcoef
            if len(data1) > 36:
                corr_coef = np.corrcoef(data1,data2)[0][1]
                if not math.isnan(corr_coef):
                    results.append((data_set[i][0] + ' and ' + data_set[j][0], corr_coef))
    return results


def data_in_common(data1, data2):
    result1, result2 = [], []
    for item1 in data1:
        for item2 in data2:
            if item1[0] == item2[0]:
                result1.append(item1[1])
                result2.append(item2[1])
                break
    return result1, result2


def add_to_plot(plot, name, dates, values, r_color = '#'+"%06x" % random.randint(0, 0xFFFFFF)):
    return plot.line(datetime(dates), values, color=r_color)

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
    if region_id == None or region_id == 0:
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
        region_name = 'the world'
        evaluate_name= 'region_name'
        unique = pd_data[evaluate_name].unique()
    else:
        evaluate_name = 'country_name'
        if region_id == 0:
            region_name = 'all countries of the world'
            unique = pd_data[evaluate_name].unique()
        else:
            region_name = pd_data.filter({'region_id':region_id})['region_name'].unique()[0]
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
        for name in all_dic:
            all_dic[name] = sort_dates(all_dic[name])
    return all_dic, item, region_name


if __name__ == "__main__":
    # main()
    main_correlation()