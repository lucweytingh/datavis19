# script that cleans the original dataset using all cleaners, saves in data/data_clean.csv

# stupid python stuff
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../..')

# init setup
from datavis19.init import *

# make sure to load original data file
pd_data = init_data("../data/data.csv")
ex_data = init_data("../data/exchange.csv")
und_data = init_data("../data/prevalence-of-undernourishment.csv")

# import all data cleaning scripts
from add_regions import *
from convert import *
from norm_items import *
from normdollar import *
from remove import *
from undernourishmentcolumn import *

# clean data, in most efficient order
print("Starting the purge!")

# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")

start_spinner("Normalizing units... (don't mind the deprecation warnings :P )")
convert_units(pd_data)
spinner.succeed()


# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
start_spinner("Normalizing items... ")
normalize_items(pd_data, items)
spinner.succeed()


#print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
start_spinner("Normalizing currency... ")
pd_data = pd_data[pd_data.country_name != "Somalia"]
pd_data = pd_data.replace("NIS", "ILS")
makenormcolumn(pd_data, ex_data)
spinner.succeed()


#print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
start_spinner("Adding regions... ")
addregions(pd_data, dic_region_id, dic_id_name)
spinner.succeed()


start_spinner("Adding undernourishment... ")
makeundercolumn(pd_data,und_data)
spinner.succeed()


# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
start_spinner("Removing unused rows... ")
pd_data = remove_rows(pd_data, remove_dict)
spinner.succeed()


# print(f"Dataset rowcount: {pd_data.shape[0]}, colcount: {pd_data.shape[1]}")
start_spinner("Done! Saving...")


# save resulting dataset
pd_data.to_csv("../data/data_clean.csv", encoding='utf-8', index=False)
spinner.succeed()

print("Done saving... im out, shoutout Jan Zwiers")
