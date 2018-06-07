from init import *
# exchange csv source = https://www.bis.org/statistics/xrusd.htm
ex_data = pd.read_csv('exchange.csv', encoding='latin-1')


# columns: country_id,country_name,city_id,city_name,market_id,market_name,item_id,item_name,cur_id,cur_name,pt_id,pt_name,unit_id,unit_name,month,year,price,source

# return the range of months in format 'yyyy-mm'
def ex_month_range(year, fr, to):
  result = []
  for j in range(fr, to+1):
    if j < 10:
          add = '0'+str(j)
    else:
      add = str(j)
    result.append(str(year) + '-' + add)
  return result

# make the columns for the exchange file (format 'yyyy-mm')
def ex_date_format(years,month_s,month_e):
  result = []
  for i in range(len(years)):
    if i == 0:
      result.append(ex_month_range(years[0],month_s, 12))
    elif i == len(years)-1:
      result.append(ex_month_range(years[-1], 1, month_e))
    else:
      result.append(ex_month_range(years[i], 1, 12))
  return [x for y in result for x in y]


def prices_month_range(year, fr, to):
  result = []
  for i in range(fr, to+1):
    result.append(((i, year)))
  return result

# make the tuples for the prices csf file (format (mm, yyyy))
def prices_date_format(years, month_s, month_e):
  result = []
  for i in range(len(years)):
    if i == 0:
      result.append(prices_month_range(years[0],month_s, 12))
    elif i == len(years)-1:
      result.append(prices_month_range(years[-1], 1, month_e))
    else:
      result.append(prices_month_range(years[i], 1, 12))
  return [x for y in result for x in y]



# convert 'yyyy-mm' to (mm, yyyy)
def totuple_format(form):
  #print(form)
  return (int(form[5:]), int(form[:4]))




# make a dictionary with dates and their dollar exchange values d
# dates = ['2007-05', '2007-06', '2007-07']
# currency = "IDR"
def currency_list_maker(currency, dates, stattype = "Average of observations through period"):
    tuples = []
    months = ex_data.filter({'CURRENCY': currency, "Collection": stattype, 'Frequency': 'Monthly'})
    for date in dates:
      tuples.append((totuple_format(date), months[date].unique()[0]))
    return tuples
  


# find the items both countries have
def shared_items(country1,country2):
  items_c1 = pd_data.filter({'country_name' : country1})["item_name"].unique()
  items_c2 = pd_data.filter({'country_name' : country2})["item_name"].unique()
  return [x for x in items_c1 if x in items_c2]

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


currency_list = [((5, 2007), 8827.727122), ((6, 2007), 8985.048179000001), ((7, 2007), 9070.863109)]
prices_list =  [((5, 2007), 8732), ((6, 2007), 9106)]

def convert_curr(currency_list, prices_list):
  dollarlist = []
  for price in prices_list:
    for currency in currency_list:
      if price[0] == currency [0]:
        dollarlist.append((price[0],int(price[1]) / int(currency[1])))
  return dollarlist

#print(convert_curr(currency_list,prices_list))

#country = 'Afghanistan' , item = 'Rice', dates = [(4,2007),(5,2007)]



dates = [(4,2007),(5,2007)]
country = "Indonesia"
item = 'Eggs'

# dates = tuples format :[(4,2007),(5,2007)], country = country name, item = for example rice
def find_prices(dates,country,item):
    prices = []
    for date in dates:
        pricedata = pd_data.filter({'country_name': country, "item_name": item, 'month': date[0] , 'year': date[1]})["price"]
        if len(pricedata.unique()) == 1:
            prices.append((date,int(pricedata.unique())))
    return prices



print(len(list(pd_data["country_name"].unique())))

 




