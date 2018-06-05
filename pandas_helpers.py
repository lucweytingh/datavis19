from helpers import *

def filter(self, params):
  for key, val in params.items():
    self = self.loc[self[key] == val]
  return self

def dict_from_column(self, column):
  dictionary = {}

  return dictionary

def get_list(self, column):
  return self[column].tolist()

# markets = {
#   "Fadde": {
#     "Rice": {
#       "price": [50, 60, 50, 40],
#       "month": [(03, 14), (04, 14), (05, 14), (06, 14)]
#     }
#   }
# }

def dict_from_columns(self, columns, results = ['price', 'month', 'year']):
  dictionary = {}

  for index, row in self.iterrows():
    values = []
    for column in columns:
      values.append(row[column])

    set_default(dictionary, values[0], {})
    for i in range(len(values)):
      if i == 0:
        continue
      set_default(dictionary, values, {})

    for result_name in results:
      result = row[result_name]
      set_default(dictionary, values + [result_name], [])
      array = get_from_dict(dictionary, values + [result_name])
      array.append(result)
      set_in_dict(dictionary, values + [result_name], array)

  return dictionary
