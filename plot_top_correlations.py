from init import *
from plot import *

corr_data = init_json('data/correlations.txt')

i = 0
for c in corr_data:
  if i > 100: break
  plot_by_market(pd_data.filter({ 'market_id': c['market_id'], 'item_name': [c['item1'], c['item2']] }), "C: {0}".format(c['correlation']))
  i += 1

i = 0
for c in reversed(corr_data):
  if i > 100: break
  plot_by_market(pd_data.filter({ 'market_id': c['market_id'], 'item_name': [c['item1'], c['item2']] }), "C: {0}".format(c['correlation']))
  i += 1