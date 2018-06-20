remove_dict = {
  "unit_name": [
    "USD/LCU", "Packet", "Month", "kWh", "Package", "Course", "Cuartilla", "MT", "Sack"
  ],
  "item_name": [
    "Wage (qualified labour)", "Wage (non-qualified labour)"
  ]
}

def remove_rows(pd_data, remove_dict):
  for column, values in remove_dict.items():
    for value in values:
      if column == "unit_name":
        pd_data = pd_data[pd_data.unit_name != value]
      elif column == "item_name":
        pd_data = pd_data[pd_data.item_name != value]
  return pd_data

if __name__ == "__main__":
  import os
  import sys
  sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
  from datavis19.init import *

  pd_data = remove_rows(pd_data, remove_dict)
  pd_data.to_csv('data/data_rows_removed.csv', encoding='utf-8', index=False)
