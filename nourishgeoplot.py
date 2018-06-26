from geochart import *
from init import *

blacklist = ['IDA only','Pacific island small states']

def datayear(year):
    reslist = []
    for index, row in und_data.iterrows():
        if row["Year"] == year and row["Entity"] not in blacklist:
            reslist.append([row["Entity"],row["POU"]])
    return reslist

#print(datayear(1999))

years = range(1992,2015)
data = []
for year in years:
    data.append(datayear(year))

print(data)

plot_geochart("undernourishment_"+ str(year), data)


