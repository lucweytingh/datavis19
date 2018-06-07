import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from helpers import *

import pandas_helpers as ph
pd.core.frame.DataFrame.filter = ph.filter
pd.core.frame.DataFrame.get_list = ph.get_list
pd.core.frame.DataFrame.dict_from_columns = ph.dict_from_columns


def init_data(filename = "region_data.csv"):
  return pd.read_csv(filename, encoding='latin-1', sep=';', dtype={'region_id': int,'region_name':str, 'country_id': int, 'country_name':str ,'city_id':int,'city_name':str,'market_id':int,'market_name':str,'item_id':int,'item_name':str,'cur_id':int,'cur_name':str,'pt_id':int,'pt_name':str,'unit_id':int,'unit_name':str,'month':int,'year':int,'price':float,'source':str})

pd_data = init_data()
