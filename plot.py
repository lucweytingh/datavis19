from init import *

def plot_data(data, columns, axes = None, title_appendix = None, blacklist = []):
  results = data.dict_from_columns(columns, axes, blacklist)
  for country, markets in results.items():
    for market, items in markets.items():
      plt.clf()
      for item, dic in items.items():
        if title_appendix == None:
          title = "{0}, {1}".format(country, market)
        else:
          title = "{0}, {1} - {2}".format(country, market, title_appendix)
        plt.title(title)
        plt.plot(dic["date"], dic["price"], label=item)
      plt.xlabel('Date')
      plt.ylabel('Price (USD)')
      plt.legend(loc='upper left')
      plt.show()

def plot_by_item(data, title_appendix = None, blacklist = []):
  plot_data(data, ['country_name', 'item_name', 'market_name'], None, title_appendix, blacklist)

def plot_by_market(data, title_appendix = None, blacklist = []):
  plot_data(data, ['country_name', 'market_name', 'item_name'], None, title_appendix, blacklist)
