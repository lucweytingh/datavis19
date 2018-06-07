import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from helpers import *

import pandas_helpers as ph
pd.core.frame.DataFrame.filter = ph.filter
pd.core.frame.DataFrame.get_list = ph.get_list
pd.core.frame.DataFrame.dict_from_columns = ph.dict_from_columns

ex_data = pd.read_csv('../exchange.csv', encoding='latin-1')


def init_data(filename = "data.csv"):
  return pd.read_csv(filename, encoding='latin-1')

pd_data = init_data()
