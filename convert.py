from init import *

# script to convert all units to less
# all original units:
# [(48, '3 KG'), (95, '168 G'), (27, 'Gallon'), (17, '90 KG'), (69, '30 pcs'), (58, 'Month'), (56, 'USD/LCU'), (28, '500 G'), (30, 'Pound'), (63, '200 G'), (74, '125 G'), (76, '18 KG'), (52, '1.5 KG'), (57, '2 KG'), (40, '85 G'), (50, 'Libra'), (98, '750 G'), (47, '3.5 KG'), (22, '50 KG'), (71, '300 G'), (41, '380 G'), (33, 'Unit'), (75, 'Packet'), (86, '11.5 KG'), (20, '100 Tubers'), (9, '100 KG'), (49, '650 G'), (96, '350 G'), (38, '750 ML'), (65, '160 G'), (36, '12.5 KG'), (55, 'Course'), (72, '185 G'), (16, '45 KG'), (83, '10 KG'), (29, 'Cuartilla'), (61, 'Head'), (97, '115 G'), (31, 'Sack'), (37, 'Loaf'), (100, 'Cubic meter'), (77, '3 L'), (43, '25 KG'), (51, 'Day'), (21, 'Bunch'), (5, 'KG'), (81, '10 pcs'), (103, '1.8 L'), (23, '91 KG'), (42, '150 G'), (87, '5 KG'), (67, '5 L'), (46, '1.8 KG'), (14, 'Marmite'), (24, '400 G'), (102, 'Package'), (15, 'L'), (19, '385 G'), (90, '12 KG'), (18, 'MT'), (99, '1.5 L'), (44, '60 KG'), (101, 'kWh'), (25, '500 ML'), (35, 'Dozen')]

conversions = {
  41: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/380)
  },
  42: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/150)
  },
  43: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/25)
  },
  44: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/60)
  },
  90: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/12)
  },
  19: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/385)
  },
  24: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/400)
  },
  46: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/1.8)
  },
  87: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/5)
  },
  23: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/91)
  },
  72: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/185)
  },
  97: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/115)
  },
  9: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/100)
  },
  83: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/10)
  },
  16: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/45)
  },
  36: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/12.5)
  },
  49: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/650)
  },
  65: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/160)
  },
  96: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/350)
  },
  86: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/11.5)
  },
  98: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/750)
  },
  47: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/3.5)
  },
  22: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/50)
  },
  71: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/300)
  },
  30: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": 0.453592
  },
  48: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/3)
  },
  95: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/168)
  },
  17: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/90)
  },
  28: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": 2
  },
  30: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": 0.453592
  },
  50: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": 0.453592
  },
  63: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": 5
  },
  74: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/125)
  },
  76: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/18)
  },
  52: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1/1.5)
  },
  57: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": 0.5
  },
  40: {
    "new_id": 5,
    "new_name": 'KG',
    "multiplier": (1000/85)
  },
  27: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": 3.78541
  },
  38: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": (1000/750)
  },
  77: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": (1/3)
  },
  103: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": (1/1.8)
  },
  67: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": (1/5)
  },
  99: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": (1/1.5)
  },
  25: {
    "new_id": 15,
    "new_name": 'L',
    "multiplier": 2
  },
  69: {
    "new_id": 33,
    "new_name": 'Unit',
    "multiplier": (1/30)
  },
  81: {
    "new_id": 33,
    "new_name": 'Unit',
    "multiplier": (1/10)
  },
  61: {
    "new_id": 33,
    "new_name": 'Unit',
    "multiplier": 1
  },
  35: {
    "new_id": 33,
    "new_name": 'Unit',
    "multiplier": (1/12)
  },
}

pd_data = pd_data.filter({ 'country_name': 'Afghanistan', 'city_name': "Fayzabad" })

print(pd_data)

for index, row in pd_data.iterrows():
  values = conversions[row['unit_id']]
  pd_data.set_value(index, 'unit_id', values['new_id'])
  pd_data.set_value(index, 'unit_name', values['new_name'])
  pd_data.set_value(index, 'price', row['price'] * values['multiplier'])

print(pd_data)
