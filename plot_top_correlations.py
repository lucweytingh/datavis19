from init import *
from plot import *

corr_data = init_json('data/correlations.txt')

item_correlations = {}

for c in corr_data:
  items = (c['item1'], c['item2'])
  set_default(item_correlations, items, [])
  if abs(c['correlation']) < 1:
    item_correlations[items].append(c['correlation'])

items_data = []

for items, corrs in item_correlations.items():
  corrs_sum = sum(corrs)
  corrs_avg = corrs_sum / len(corrs)
  items_data.append([items, corrs_sum, corrs_avg])

amount = 10

print("Top {0} positive correlations sorted by sum of correlations:".format(amount))
i = 0
for items in sorted(items_data, key=lambda x: x[1], reverse=True):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

print("Top {0} positive correlations sorted by average of correlations:".format(amount))
i = 0
for items in sorted(items_data, key=lambda x: x[2], reverse=True):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

print("Top {0} negative correlations sorted by sum of correlations:".format(amount))
i = 0
for items in sorted(items_data, key=lambda x: x[1], reverse=False):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

print("Top {0} negative correlations sorted by average of correlations:".format(amount))
i = 0
for items in sorted(items_data, key=lambda x: x[2], reverse=False):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

# amount = 200

# i = 0
# for c in corr_data:
#   if i > amount: break
#   plot_by_market(pd_data.filter({ 'market_id': c['market_id'], 'item_name': [c['item1'], c['item2']] }), "C: {0}".format(c['correlation']))
#   i += 1

# i = 0
# for c in reversed(corr_data):
#   if i > amount: break
#   plot_by_market(pd_data.filter({ 'market_id': c['market_id'], 'item_name': [c['item1'], c['item2']] }), "C: {0}".format(c['correlation']))
#   i += 1
