from init import *
# from plot import *

corr_data = init_json('data/correlations.txt')
print(len(corr_data))

item_correlations = {}

for c in corr_data:
  items = (c['item1'], c['item2'])
  set_default(item_correlations, items, [])
  if abs(c['correlation']) < 1:
    item_correlations[items].append(c['correlation'])

items_data = []

pos = 0
neg = 0
no = 0

for items, corrs in item_correlations.items():
  corrs_sum = sum(corrs)
  corrs_avg = corrs_sum / len(corrs)
  if corrs_sum != corrs_avg:
    items_data.append([items, corrs_sum, corrs_avg])
  if corrs_avg > 0:
    pos += 1
  if corrs_avg < 0:
    neg += 1
  if abs(corrs_avg) < 0.1:
    no += 1

print(len(items_data))
print(pos)
print(neg)
print(no)
amount = 50

print("Top {0} positive correlations sorted by sum of correlations:".format(amount))
i = 0
itemsset = []
for items in sorted(items_data, key=lambda x: x[1], reverse=True):
  if i > amount: break
  itemsset.append(items[0])
  print("{0} & {1} & {2} & {3}".format(items[0][0], items[0][1], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
[print("({0} en {1})".format(items[0], items[1])) for items in itemsset]
print("")

print("Top {0} positive correlations sorted by average of correlations:".format(amount))
i = 0
itemsset = []
for items in sorted(items_data, key=lambda x: x[2], reverse=True):
  if i > amount: break
  itemsset.append(items[0])
  print("{0} & {1} & {2} & {3}".format(items[0][0], items[0][1], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
[print("({0} en {1})".format(items[0], items[1])) for items in itemsset]
print("")

print("Top {0} negative correlations sorted by sum of correlations:".format(amount))
i = 0
itemsset = []
for items in sorted(items_data, key=lambda x: x[1], reverse=False):
  if i > amount: break
  itemsset.append(items[0])
  print("{0} & {1} & {2} & {3}".format(items[0][0], items[0][1], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
[print("({0} en {1})".format(items[0], items[1])) for items in itemsset]
print("")

print("Top {0} negative correlations sorted by average of correlations:".format(amount))
i = 0
itemsset = []
for items in sorted(items_data, key=lambda x: x[2], reverse=False):
  if i > amount: break
  itemsset.append(items[0])
  print("{0} & {1} & {2} & {3}".format(items[0][0], items[0][1], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
[print("({0} en {1})".format(items[0], items[1])) for items in itemsset]
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
