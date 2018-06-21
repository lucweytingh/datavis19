from init import *
from geochart import *

volatilities = []

for country, df in pd_data.split('country_name').items():
  volatility = df.sum_of_difference('price_usd') / len(df)
  if np.isnan(volatility):
    volatility = 0
  volatilities.append([country, volatility])


for vol in sorted(volatilities, key=lambda x: x[1], reverse=True):
  print("{0}: {1}".format(vol[0], vol[1]))

plot_geochart("volatility", volatilities)
