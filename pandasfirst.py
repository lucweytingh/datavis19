from init import *


print(ph.filter(ph.filter(pd_data, 'country_id', 1),'item_id',145)['price'])