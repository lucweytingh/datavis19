from init import *

def plot_data(data, columns, axes = None, blacklist = []):
  results = data.dict_from_columns(columns, axes, blacklist)

  for market, items in results.items():
    plt.clf()
    for item, dic in items.items():
      plt.title(f"{market}")
      plt.plot(dic["date"], dic["price"], label=item)
    plt.legend(loc='upper right')
    plt.show()

def plot_by_item(data, blacklist = []):
  plot_data(data, ['item_name', 'market_name'], None, blacklist)

def plot_by_market(data, blacklist = []):
  plot_data(data, ['market_name', 'item_name'], None, blacklist)
