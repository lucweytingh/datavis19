import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from helpers import *

import pandas_helpers as ph
pd.core.frame.DataFrame.filter = ph.filter
pd.core.frame.DataFrame.get_list = ph.get_list
pd.core.frame.DataFrame.dict_from_columns = ph.dict_from_columns
pd.core.frame.DataFrame.sum_of_difference = ph.sum_of_difference

def init_data(filename = "region_data.csv"):
  return pd.read_csv(filename, encoding='latin-1')

ex_data = init_data('exchange.csv')
pd_data = init_data()