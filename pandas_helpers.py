from datavis19.helpers import *
import datetime

def filter(self, params):
  for key, val in params.items():
    if val.__class__ == [].__class__:
      self = self.loc[self[key].isin(val)]
    else:
      self = self.loc[self[key] == val]
  return self

def split(self, column):
  return dict(tuple(self.groupby(column)))

def sum_of_difference(self, column):
  sum = 0
  prevrow = None
  none_class = None.__class__
  for index, row in self.iterrows():
    if not index == 0:
      if not (row.__class__ == none_class or prevrow.__class__ == none_class):
        sum += abs(row[column] - prevrow[column])
    prevrow = row
  return sum

def dict_from_columns(self, columns, results = None, blacklist = []):
  if results == None: results = ['price', 'date']
  dictionary = {}

  if len(columns) == 0:
    for result in results:
      dictionary[result] = self.get_list(result)
  else:
    column = columns[0]
    dfs = self.split(column)
    for value in list(set(self[column])):
      data = dfs[value]
      dictionary[value] = data.dict_from_columns(columns[1:], results, blacklist)

  return dictionary

def get_list(self, column):
  if column == 'date':
    return [datetime.datetime(year, month, 1) for year, month in zip(self['year'], self['month'])]
  if column == 'date_and_price':
    return [(date, price) for date, price in zip(self.get_list('date'), self['price'])]
  if column == 'avg_price_per_date':
    result = []
    for year, months in self.dict_from_columns(['year', 'month'], ['price_usd']).items():
      for month, prices in months.items():
        p = prices['price_usd']
        avg = sum(p) / len(p)
        result.append((datetime.datetime(year, month, 1), avg))
    return result

  return self[column].tolist()
