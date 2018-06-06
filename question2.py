from init import *
import exchange_finder
ex_data = pd.read_csv('../exchange.csv', encoding='latin-1')


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


print(prices_date_format([1999,2000,2001,2002], 3, 5))

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


def convert_curr(exchange, currency):
  return [x/y for x in currency for y in exchange]



# def price_diff(country1, country2, item):
#     # print item name
#     print(pd_data.filter({'item_name': item,['item_name'].unique()[0])
    
#     sharedyears, month_s, month_e = shared_months(country1,country2, item)

#     ex_columns = ex_date_format(sharedyears, month_s, month_e)

    # find currencies for countries



#     currency_dictionary_maker()




dates = [(3, 1999), (4, 1999), (5, 1999), (6, 1999), (7, 1999), (8, 1999), (9, 1999), (10, 1999), (11, 1999), (12, 1999), (1, 2000), (2, 2000),(3, 2000), (4, 2000), (5, 2000), (6, 2000), (7, 2000), (8, 2000), (9, 2000), (10, 2000), (11, 2000), (12, 2000), (1, 2001), (2, 2001), (3, 2001), (4, 2001), (5, 2001), (6, 2001), (7, 2001), (8, 2001), (9, 2001), (10, 2001), (11, 2001), (12, 2001), (1, 2002), (2, 2002), (3, 2002), (4, 2002), (5, 2002)]
country = "Indonesia"
item = 'Eggs'



def find_prices(dates,country,item):
    for date in dates:
        print(date)
        row = pd_data.filter({'country_name': country, "item_name": item, 'month': date[0] , 'year': date[1]})
        print(row)
    
#find_prices(dates,country,item)

date = (3,1999)
print(pd_data.filter({'country_name': country, "item_name": item, 'month': date[0] , 'year': date[1]}))


#  def currency_finder(country):







# price_diff('Indonesia','Philippines')

# print(pd_data.filter({'country_name' : 'Indonesia', 'item_id': 84})["item_id"])
# print(pd_data.filter({'country_name' : 'Indonesia'})["item_id"].unique())

#print(price_diff("mais","Philippines","Indonesia",265.325))