from init import *


# print(ph.filter(ph.filter(pd_data, 'country_id', 1),'item_id',145)['price'])


# pd_data1 = pd_data.var()


# print(pd_data1((pd_data1.country_id == 1) & (pd_data1.item_id == 145)))

print(ph.filter(pd_data, {'country_id':1, 'item_id':284}))