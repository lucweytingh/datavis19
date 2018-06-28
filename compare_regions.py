from init import *
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend
#import simplejson


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
        
def main_correlation_plot():
    items = ['Tomatoes']# pd_data['item_name'].unique()
    regions = [0]
    correlation(regions, items, 10)

def main_correlation_raw():
    items = pd_data['item_name'].unique()
    compare_to_global(items)


def compare_to_global(items):
    global_data = gather_data([0], items)
    item_amount = len(items)
    points_for_regions = 0
    points_for_global = 0

    for item_data in global_data:
        highest, lowest = find_top_corr([item_data], 5)
        for item in highest:
            index = item[1][0].find(' and ')
            if same_region(item[1][0][:index], item[1][0][index + 5:]):
                points_for_regions += 1
            else:
                points_for_global += 1

    print('points for global ', points_for_global)
    print('points for regions ', points_for_regions)
    
    if points_for_global > points_for_regions:
        print("There does not seem to be a significant relation between countries in the same region.")
    else:
        print("It seems that there is a significant relation between countries in the same region.")

def same_region(country1, country2):
    return pd_data.filter({'country_name':country2})['region_name'].unique()[0] == pd_data.filter({'country_name':country1})['region_name'].unique()[0]

        
# plot the top given amount of pos & neg correlations of given items in given regions
def correlation(regions, items, amount):
    data_sets = gather_data(regions, items) #simplejson.load(open("data/global_data2.txt")) # gather_data(regions, items)
    # file1 = open("global_data2.txt", 'w')
    # simplejson.dump(data_sets, file1)
    # file1.close()
    print("")
    print("Finding top correlation..")
    top_corr_high, top_corr_low = find_top_corr(data_sets, amount)
    plot_results(data_sets, top_corr_high + top_corr_low)



def gather_data(regions, items):
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
    return data_sets

def plot_results(data_sets, corr_list):
    for corr in corr_list:
        data = find_data_set(corr[0], data_sets)
        plot1 = figure(x_axis_type="datetime", title="Average price of " + corr[0][0].lower() + ':' + ' a correlation of ' + str(corr[1][1]))
        legend = []
        colors = ['#e6194b', '#0082c8', '#911eb4', '#3cb44b', '#46f0f0']
        count = 0
        for name in data:
            if name in corr[1][0]:
                if data[name] != []:
                    dates, values = split_date_and_values(data[name])
                    if corr[0][1] != 'the world':
                        region = pd_data.filter({'country_name':name})['region_name'].unique()[0]
                        legend.append((name + ' (' + region + ')', [add_to_plot(plot1, dates, values, colors[count])]))
                    else:    
                        legend.append((name, [add_to_plot(plot1, dates, values, colors[count])]))
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
    if input_list == []:
        if max_length >= len(win_list):
            min = 0
        else:
            min = len(win_list) - max_length
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
    if max_length >= len(win_list):
        min = 0
    else:
        min = len(win_list) - max_length
    return win_list[:max_length], win_list[min:][::-1]


# return the  
def find_top_corr(data_sets, amount):
    if amount == None:
        amount = sys.maxsize
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


def add_to_plot(plot, dates, values, r_color = '#'+"%06x" % random.randint(0, 0xFFFFFF)):
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

# returns shared years, starting month and end month of certain item
def shared_months(country1,country2, item):
  # find all shared years for item
    years_c1 = pd_data.filter({'item_name': item, 'country_name': country1})['year'].unique()
    years_c2 = pd_data.filter({'item_name': item, 'country_name': country2})['year'].unique()
    sharedyears = [x for x in years_c1 if x in years_c2]

    # find shared start month in first year
    months_c1 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[0]})['month'].unique()
    months_c2 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[0]})['month'].unique()
    sharedmonths = [x for x in months_c1 if x in months_c2]
    month_s = sharedmonths[0]

    # find shared last month in last year
    months_c1 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[-1]})['month'].unique()
    months_c2 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[-1]})['month'].unique()
    sharedmonths = [x for x in months_c1 if x in months_c2]
    month_e = sharedmonths[-1]
    return sharedyears, month_s, month_e

# find the items both countries have
def shared_items(country1,country2):
  items_c1 = pd_data.filter({'country_name' : country1})["item_name"].unique()
  items_c2 = pd_data.filter({'country_name' : country2})["item_name"].unique()
  return [x for x in items_c1 if x in items_c2]

if __name__ == "__main__":
    from bokeh.layouts import gridplot
    from bokeh.plotting import figure, show, output_file
    from bokeh.models import Legend
    # test_dates = [((1, 2006), 0.2768810516701759), ((2, 2006), 0.28593047558787704), ((3, 2006), 0.28802077470255943), ((4, 2006), 0.28738613596635715), ((5, 2006), 0.2860767156720411), ((6, 2006), 0.29261475828304473), ((7, 2006), 0.27963102968064624), ((11, 2006), 0.32396098841041737), ((1, 2004), 0.2527255874820858), ((2, 2004), 0.2596318750083353), ((3, 2004), 0.2576683009971368), ((4, 2004), 0.2674213554900618), ((5, 2004), 0.25713157618574906), ((6, 2004), 0.25772099841343993), ((7, 2004), 0.2580106042676619), ((8, 2004), 0.2551941803997591), ((9, 2004), 0.2589134990052946), ((10, 2004), 0.2597369740466546), ((11, 2004), 0.28608626565652484), ((12, 2004), 0.27836322846993933), ((1, 2005), 0.26436998595299055)]
    # test_dates = sort_dates(test_dates)
    # dates, values = split_date_and_values(test_dates)
    # print(dates)
    # main()
