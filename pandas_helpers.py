from datavis19.helpers import *
import datetime

def filter(self, params):
  for key, val in params.items():
    if val.__class__ == [].__class__:
      self = self.loc[self[key].isin(val)]
    else:
      self = self.loc[self[key] == val]
  return self

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

  for index, row in self.iterrows():
    values = get_row_values(row, columns, blacklist)

    if values:
      set_default(dictionary, values[0], {})
      for i in range(len(values)):
        if i == 0:
          continue
        set_default(dictionary, values, {})

      for result_name in results:
        if result_name == 'date':
          # custom result for custom 'date' field
          result = datetime.datetime(row['year'], row['month'], 1)
        else:
          result = row[result_name]
        set_default(dictionary, values + [result_name], [])
        array = get_from_dict(dictionary, values + [result_name])
        array.append(result)
        set_in_dict(dictionary, values + [result_name], array)

  return dictionary

def get_row_values(row, columns, blacklist):
  values = []
  for column in columns:
      if column == 'date':
        # custom result for custom 'date' field
        column_value = datetime.datetime(row['year'], row['month'], 1)
      else:
        column_value = row[column]

      if column_value in blacklist: return False
      values.append(column_value)
  return values

def get_list(self, column):
  return self[column].tolist()
