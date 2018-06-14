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

# pd_data = pd_data.filter({ 'country_name': 'Haiti' })

markets = list(set(pd_data['market_name']))
items = list(set(pd_data['item_name']))

# markets = ['Medellin']

pd_data_copy = pd_data

results = {}

for market in markets:
  pd_data_market = pd_data.filter({ 'market_name': market })
  items = list(set(pd_data_market['item_name']))
  for item in items:
    pd_data_item = pd_data_market.filter({ 'item_name': item })

    if not pd_data_item.empty:
      dates = [datetime.datetime(year, month, 1) for year, month in zip(pd_data_item['year'], pd_data_item['month'])]

      set_default(results, market, [])

      results[market].append({
        'market': market,
        'name': item,
        'dates_and_prices': [(date, price) for date, price in zip(dates, list(pd_data_item['price']))],
        'dates': dates
      })

relative_item_data = []

for market, market_results in results.items():
  for i in range(len(market_results)):
    item = market_results[i]
    rest = market_results[i+1:]

    for item2 in rest:
      dates = set(item['dates']).intersection(set(item2['dates']))
      item_prices  = [dandp[1] for dandp in item['dates_and_prices']  if dandp[0] in dates]
      item2_prices = [dandp[1] for dandp in item2['dates_and_prices'] if dandp[0] in dates]

      if len(item_prices) >= 12 and len(item_prices) == len(item2_prices):
        corrcoef = np.corrcoef(item_prices, item2_prices)[0][1]
        if not np.isnan(corrcoef):
          relative_item_data.append({
            'market': market,
            'item1': item['name'],
            'item2': item2['name'],
            'correlation': corrcoef
          })

relative_item_data.sort(key=lambda x: x['correlation'], reverse=True)

# save as json
import json
with open('data/correlations.txt', 'w') as f:
  json.dump(relative_item_data, f, ensure_ascii=False)

print("Largest positive correlations:")
for corr in relative_item_data[:9]:
  plot_by_market(pd_data.filter({ 'market_name': corr['market'], 'item_name': [corr['item1'], corr['item2']] }))
  print(f"C: {corr['correlation']}, {corr['item1']} and {corr['item2']}")
print("")
print("Largest negative correlations:")
for corr in reversed(relative_item_data[-9:]):
  plot_by_market(pd_data.filter({ 'market_name': corr['market'], 'item_name': [corr['item1'], corr['item2']] }))
  print(f"C: {corr['correlation']}, {corr['item1']} and {corr['item2']}")

