from init import *

def plot_data(filter, columns, axes = None, blacklist = []):
  results = pd_data.filter(filter).dict_from_columns(columns, axes, blacklist)

  for market, items in results.items():
    plt.clf()
    for item, dic in items.items():
      print(item)
      print(dic)
      plt.title(f"{market}")
      plt.plot(dic["date"], dic["price"], label=item)
    plt.legend(loc='upper right')
    plt.show()

def plot_by_item(filter):
  plot_data(filter, ['item_name', 'market_name'])

def plot_by_market(filter):
  plot_data(filter, ['market_name', 'item_name'])


plot_by_item({ 'country_name': 'Niger' })
