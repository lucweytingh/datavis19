import pandas

import numpy as np

data = pandas.read_csv("foodprices.csv",     encoding='latin-1')

print(data.mode()["cm_id"])