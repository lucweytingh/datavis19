from geochart import *
from init import *

blacklist = ['IDA only','Pacific island small states', 'Other small states', 'Small states', 'Middle income', 'Middle East & North Africa (excluding high income)','Low income']

def datayear(year):
    reslist = []
    for index, row in und_data.iterrows():
        if row["Year"] == year and row["Entity"] not in blacklist:
            reslist.append([row["Entity"],row["POU"]])
    return reslist

#print(datayear(1999))

years = range(1991,2015)
data = []
for year in years:
    data.append(datayear(year))


plot_geochart("undernourishment_geochart", data, {"labels":list(range(1991,2015))})


