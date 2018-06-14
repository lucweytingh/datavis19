# script that cleans the original dataset using all cleaners, saves in data/data_clean.csv

# stupid python stuff
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

# init setup
from datavis19.init import *

# make sure to load original data file
pd_data = init_data("data/data.csv")

# import all data cleaning scripts
from add_regions import *
from convert import *
from norm_items import *
from normdollar import *
from remove import *

# clean data, in most efficient order
print("Starting the purge!")

print("")
# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
print("Removing unused rows... ")
pd_data = remove_rows(pd_data, remove_dict)

print("")
# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
print("Normalizing units... (don't mind the deprecation warnings :P )")
convert_units(pd_data)

print("")
# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
print("Normalizing items... ")
normalize_items(pd_data, items)

print("")
#print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
print("Normalizing currency... ")
pd_data = pd_data[pd_data.country_name != "Somalia"]
pd_data = pd_data.replace("NIS", "ILS")
makenormcolumn(pd_data, ex_data)

print("")
#print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
print("Adding regions... ")
addregions(pd_data, dic_region_id, dic_id_name)

print("")
# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
print("Done! Saving...")

# save resulting dataset
pd_data.to_csv("data/data_clean.csv", encoding='utf-8', index=False)

print("")
print("Done saving... im out, shoutout Jan Zwiers")
