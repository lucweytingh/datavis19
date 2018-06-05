import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas_helpers as ph

def init_data(filename = "data.csv"):
  return pd.read_csv(filename, encoding='latin-1')

pd_data = init_data()
