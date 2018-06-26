from functools import reduce  # forward compatibility for Python 3
import operator
import os

from math import sqrt

def get_from_dict(dictionary, keys_list):
  return reduce(operator.getitem, keys_list, dictionary)

def set_in_dict(dictionary, keys_list, value):
  get_from_dict(dictionary, keys_list[:-1])[keys_list[-1]] = value

def set_default(dictionary, values, default):
  if values.__class__ == list().__class__:
    if values[-1] not in get_from_dict(dictionary, values[:-1]).keys():
      set_in_dict(dictionary, values, default)
  else:
    if values not in dictionary.keys():
      dictionary[values] = default

def i_sqrt(n, i):
  if i == 0: return n
  return sqrt(i_sqrt(n, i - 1))

def create_dir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
