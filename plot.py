from init import *

def plot_data(data, columns, axes = None, title = None, blacklist = []):
  results = data.dict_from_columns(columns, axes, blacklist)
  for market, items in results.items():
    plt.clf()
    for item, dic in items.items():
      if title == None:
        title = market
      else:
        title = "{0}, {1}".format(market, title)
      plt.title(title)
      plt.plot(dic["date"], dic["price"], label=item)
    plt.legend(loc='upper right')
    plt.show()

def plot_by_item(data, title = None, blacklist = []):
  plot_data(data, ['item_name', 'market_name'], None, title, blacklist)

def plot_by_market(data, title = None, blacklist = []):
  plot_data(data, ['market_name', 'item_name'], None, title, blacklist)
