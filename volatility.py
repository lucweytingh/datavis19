from init import *

volatilities = []

for country, df in pd_data.split('country_name').items():
  volatility = df.sum_of_difference('price_usd') / len(df)
  volatilities.append((country, volatility))


for vol in sorted(volatilities, key=lambda x: x[1], reverse=True):
  print("{0}: {1}".format(vol[0], vol[1]))
