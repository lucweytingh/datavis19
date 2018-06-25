# Are there any food prices that are show negative/positive correlation, and is this correlation present throughout the years, or perhaps only in certain period? Can you perhaps detect possible ingredients of a certain other food product?

import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

from init import *
from plot import *

markets = list(set(pd_data['market_id']))
items = list(set(pd_data['item_name']))

results = pd_data.dict_from_columns(['country_name', 'market_id', 'item_name'], ['date', 'avg_price_per_date'])

relative_item_data = []

for country_name, country_results in results.items():
  for market, market_results in country_results.items():
    market_results = list(market_results.items())
    for i in range(len(market_results)):
      item_data = market_results[i]
      rest = market_results[i+1:]

      for item2_data in rest:
        item_name = item_data[0]
        item = item_data[1]
        item2_name = item2_data[0]
        item2 = item2_data[1]

        item_dates = item['date']
        item2_dates = item2['date']
        dates = [date for date in item_dates if date in item2_dates]
        item_prices  = [dandp[1] for dandp in item['avg_price_per_date']  if dandp[0] in dates]
        item2_prices = [dandp[1] for dandp in item2['avg_price_per_date'] if dandp[0] in dates]

        if len(item_prices) != len(item2_prices) and len(item_prices) <= 5:
          print("dates:")
          print(dates)
          print("item1:")
          print(item['avg_price_per_date'])
          print("item2:")
          print(item2['avg_price_per_date'])
          print("Date: {0}, item1: {1}, item2: {2}".format(len(dates), len(item_prices), len(item2_prices)))

        if len(item_prices) >= 12 and len(item_prices) == len(item2_prices):
          corrcoef = np.corrcoef(item_prices, item2_prices)[0][1]
          if not np.isnan(corrcoef):
            relative_item_data.append({
              'country_name': country_name,
              'market_id': market,
              'item1': item_name,
              'item2': item2_name,
              'correlation': corrcoef
            })

relative_item_data.sort(key=lambda x: x['correlation'], reverse=True)

# save as json
import json
with open('data/correlations.txt', 'w') as f:
  json.dump(relative_item_data, f, ensure_ascii=False)

print("Largest positive correlations:")
for corr in relative_item_data[:9]:
  plot_by_market(pd_data.filter({ 'market_id': corr['market_id'], 'item_name': [corr['item1'], corr['item2']] }))
  print(f"C: {corr['correlation']}, {corr['item1']} and {corr['item2']}")
print("")
print("Largest negative correlations:")
for corr in reversed(relative_item_data[-9:]):
  plot_by_market(pd_data.filter({ 'market_id': corr['market_id'], 'item_name': [corr['item1'], corr['item2']] }))
  print(f"C: {corr['correlation']}, {corr['item1']} and {corr['item2']}")
