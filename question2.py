from init import *
# exchange csv source = https://www.bis.org/statistics/xrusd.htm


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


# print(prices_date_format([1999,2000,2001,2002], 3, 5))

# convert 'mm-yyyy' to (mm, yyyy)
def totuple_format(form):
  return (int(form[:2]), int(form[3:]))

# make a dictionary with dates and their dollar exchange values
def currency_dictionary_maker(currency, dates, stattype = "Average of observations through period"):
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




# dates = [(1, 2012), (2, 2012), (3, 2012), (4, 2012), (5, 2012), (6, 2012), (7, 2012), (8, 2012), (9, 2012), (10, 2012), (11, 2012), (12, 2012), (1, 2013), (2, 2013), (3, 2013), (4, 2013), (5, 2013), (6, 2013), (7, 2013), (8, 2013), (9, 2013), (10, 2013), (11, 2013), (12, 2013), (1, 2014)]
# country = "Indonesia"
# item = 'Eggs'

# def find_prices(dates,country,item):
#     prices = []
#     for date in dates:
#         pricedata = pd_data.filter({'country_name': country, "item_name": item, 'month': date[0] , 'year': date[1]})["price"]
#         if len(pricedata.unique()) == 1:
#             prices.append((date,int(pricedata.unique())))
#     return prices
    
print(find_prices(dates,country,item))


 








# price_diff('Indonesia','Philippines')

# print(pd_data.filter({'country_name' : 'Indonesia', 'item_id': 84})["item_id"])
# print(pd_data.filter({'country_name' : 'Indonesia'})["item_id"].unique())

#print(price_diff("mais","Philippines","Indonesia",265.325)) 