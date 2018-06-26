from init import *
from geochart import *

def main():
    # item, date = item_and_data_in_common()
    item = 'Rice'


    avg_price_visual(item)
    
def avg_price_visual(item_name):
    data = pd_data.filter({'item_name':item_name})
    years = list(set(data['year'].unique()))
    begin_month = list(set(data.filter({'year':years[0]})['month'].unique()))[0]
    end_month = list(set(data.filter({'year':years[-1]})['month'].unique()))[-1]
    data_r = data_range(years, begin_month, end_month)
    all_data = []
    curr_year = 0
    for date in data_r:
        if date[1] != curr_year:
            # if curr_year != 0:
                # spinner.succeed()
            # start_spinner('Retrieving data for ' + str(date[1]) + '...')
            print('Retrieving data for the year ' + str(date[1]))
            curr_year = date[1]
        all_data.append([[x[0], i_sqrt(x[1], 10)] for x in avg_price_country(item_name, date)])
    plot_geochart('average_price_of_' + item_name.lower(), all_data, {'framerate':4})


def data_range(years, begin_month, end_month):
    result = []
    years_len = len(years)
    for i in range(years_len):
        if i == 0:
            for j in range(begin_month, 13):
                result.append((j, years[i]))
        elif i == years_len - 1:
            for j in range(1, end_month + 1):
                result.append((j, years[i]))
        else:
            for j in range(1, 13):
                result.append((j, years[i]))
    return result
    
def avg_price_country(item_name, date):
    data = pd_data.filter({'item_name':item_name, 'month':date[0],'year':date[1]})
    prices = data.get_list('price_usd')
    countries = data.get_list('country_name')
    occurrence_dic = count_occurrences(countries)
    rem_list = []
    len_countries = len(countries)
    for i in range(len_countries):
        for j in range(i+1, len_countries):
            if countries[i] == countries[j] and i not in rem_list and j not in rem_list:
                prices[i] += prices[j]
                rem_list.append(j)
    countries = rem_indeces(countries, rem_list)
    prices = rem_indeces(prices, rem_list)
    country_prices = []
    for i in range(len(countries)):
        if not np.isnan(prices[i]):
            country_prices.append([countries[i], prices[i]])
    return [[z[0], z[1] / occurrence_dic[z[0]]] for z in country_prices]

# delete all indeces from input list given in an indeces list
def rem_indeces(input, indeces):
    indeces.sort()
    for i in range(len(indeces)):
        del(input[indeces[i]-i])
    return input


def count_occurrences(items):
    result = {}
    for item in set(items):
        result[item] = items.count(item)
    return result




if __name__ == "__main__":
    main()
