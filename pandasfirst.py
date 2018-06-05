import pandas

import numpy as np

data = pandas.read_csv("data.csv",     encoding='latin-1')

print(data.mode()["country_id"])