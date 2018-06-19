import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os.path
import random

import json

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../..'))

import datavis19.config as config

from datavis19.helpers import *
import bokeh

import datavis19.pandas_helpers as ph
pd.core.frame.DataFrame.filter = ph.filter
pd.core.frame.DataFrame.get_list = ph.get_list
pd.core.frame.DataFrame.dict_from_columns = ph.dict_from_columns
pd.core.frame.DataFrame.sum_of_difference = ph.sum_of_difference


def init_data(filename):
  if os.path.isfile(filename):
    if filename == "data.csv":
      encoding = "latin-1"
    else:
      encoding = "utf-8"
    return pd.read_csv(filename, encoding=encoding, low_memory = False)
  else:
    return None

def init_json(filename):
  if os.path.isfile(filename):
    with open(filename) as json_data:
      return json.load(json_data)
  else:
    return None

ex_data = init_data('data/exchange.csv')
pd_data = init_data(config.PD_DATA_FILENAME)
und_data = init_data('data/prevalence-of-undernourishment.csv')
