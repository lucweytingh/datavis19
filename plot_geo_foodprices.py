from init import *
from geochart import *

def main():
    # item, date = item_and_data_in_common()
    item = 'Wheat'

    data = avg_price_country(item, (1,2010))

    filename = plot_geochart('price_of_' + item.lower(), [[z[0], i_sqrt(z[1], 10)] for z in data])
    html_to_png(filename, 'price_of_' + item.lower() + '.png')

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
