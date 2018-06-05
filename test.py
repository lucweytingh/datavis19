from init import *

results = pd_data.filter({ 'country_id': 1, 'city_id': 272 }).dict_from_columns(['market_name', 'item_name'])

for market, items in results.items():
  for item, dic in items.items():
    prices = dic["price"]
    dates = list(zip(dic["month"], dic["year"]))
    plt.plot(dates, prices)
    break
  plt.show()

# pd_data = pd_data.filter({ 'country_id': 1 }).groupby('market_name').groupby('product_name')[['month', 'year', 'price', 'product_name']]

# pd_data.plot(x=['month', 'year'], y='price')

# plt.show()

# markets = pd_data.dict_from_column('market_name')

# for market in markets:

#   plt.show()


# plt.plot([x1...xn], [y1...yn])

# dates = [(year, month), (year, month)]
# y = prices
# x = [datetime(year, month) for year, month in dates]
# startdate = datetime(year, month)
# x = [startdate + datetime.timedelta(month=i) for i in range(len(y))]
