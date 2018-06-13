from init import *

def unitcounter():
    units = pd_data["unit_name"].unique()
    for unit in units:#
        inst = pd_data.filter({"unit_name":unit}).get_list('unit_name')
        print(unit,end="")
        print(" :  ",end="")
        print(len(inst))
        
inst =  pd_data.filter({"unit_name": "KG"}).get_list('unit_name')       
print(len(inst))

# print(pd_data.filter({"unit_name": 'eggs'})["item_name"])



