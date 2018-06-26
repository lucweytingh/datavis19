from init import *
from geochart import *

total = []

for country, df in pd_data.split('country_name').items():
  rows = df.shape[0]
  total.append([country, rows])

# total = list(map(lambda x: [x[0], i_sqrt(x[1], 10)], total))

# for vol in sorted(volatilities, key=lambda x: x[1], reverse=True):
#   print("{0}: {1}".format(vol[0], vol[1]))

plot_geochart("total_rows", total, False, { "label_prepend": "Amount of rows per country" })
