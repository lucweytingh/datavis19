
def totuple_format(form):
  return (int(form[5:]), int(form[:4]))


def currency_list_maker(ex_data, currency, dates, stattype = "Average of observations through period"):
    tuples = []
    months = ex_data.filter({'CURRENCY': currency, "Collection": stattype, 'Frequency': 'Monthly'})
    for date in dates:
      tuples.append((totuple_format(date), months[date].unique()[0]))
    return tuples

def to_exchange_format(list):
    exchangeform = []
    for tuple in list:
        if len(str(tuple[0])) != 1:
            exchangeform.append(str(tuple[1])+'-'+str(tuple[0]))
        else:
            exchangeform.append(str(tuple[1])+'-0'+str(tuple[0]))
    return exchangeform


def datemaker(pd_data, country):
    months = pd_data.filter({'country_name':country})['month'].tolist()
    years = pd_data.filter({'country_name':country})['year'].tolist()
    return list(zip(months,years))


def makenormcolumn(pd_data, ex_data):
    normlist = []
    countries = pd_data['country_name'].unique()
    for country in countries:
        country_data = pd_data.filter({'country_name':country})
        currency = country_data['cur_name'].unique()[0]
        dates = datemaker(pd_data, country)
        datesexc = to_exchange_format(dates)
        currency_list = currency_list_maker(ex_data, currency,datesexc)
        prices_list = list(zip(dates,country_data["price"]))
        countrylist = convert_curr(currency_list,prices_list)
        normlist.extend(countrylist)
    with open("newcolumn.txt", "w") as f:
        for s in normlist:
            f.write(str(s) +"\n")

    pd_data['price_usd'] = normlist

def convert_curr(currency_list, prices_list):
  dollarlist = []
  for i in range(len(currency_list)):
    dollarlist.append(prices_list[i][1]/currency_list[i][1])
  return dollarlist


if __name__ == "__main__":
  import os
  import sys
  sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
  from datavis19.init import *
  makenormcolumn(pd_data)
  pd_data.to_csv('data/data_currency_norm.csv', encoding='utf-8', index=False)







