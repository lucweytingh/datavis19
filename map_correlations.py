from init import *
from plot import *
from geochart import *

corr_data = init_json('data/correlations.txt')
print(len(corr_data))

country_corrs = {}

for c in corr_data:
  set_default(country_corrs, c['country_name'], [])
  if abs(c['correlation']) < 1:
    country_corrs[c['country_name']].append(c['correlation'])

country_data = []
country_geodata = []

for country, corrs in country_corrs.items():
  corrs_sum = sum(corrs)
  corrs_avg = corrs_sum / len(corrs)
  country_data.append([country, corrs_sum, corrs_avg])
  country_geodata.append([country, corrs_avg])

plot_geochart("avg_country_corrs", country_geodata)

amount = 10

print("Top {0} positive correlations sorted by sum of correlations:".format(amount))
i = 0
for items in sorted(country_data, key=lambda x: x[1], reverse=True):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

print("Top {0} positive correlations sorted by average of correlations:".format(amount))
i = 0
for items in sorted(country_data, key=lambda x: x[2], reverse=True):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

print("Top {0} negative correlations sorted by sum of correlations:".format(amount))
i = 0
for items in sorted(country_data, key=lambda x: x[1], reverse=False):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")

print("Top {0} negative correlations sorted by average of correlations:".format(amount))
i = 0
for items in sorted(country_data, key=lambda x: x[2], reverse=False):
  if i > amount: break
  print("{0}, sum: {1}, avg: {2}".format(items[0], '%.2f' % items[1], '%.2f' % items[2]))
  i += 1
print("")
