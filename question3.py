from init import *




def food_data(country):
    food_data = {}
    data = pd_data.filter({'country_name':country})
    for index, row in data.iterrows():
        item = row["item_name"]
        status = 0
        if item in food_data:
            for stat in food_data[item]:
                if stat[0] == (row["month"],row["year"]):
                    status = 1
                    stat[1][0].append(row["price_usd"])
        if status == 0 and item in food_data:
            food_data[item].append(((row["month"],row["year"]),[[row["price_usd"]],row["undernourishment"]]))
        if item not in food_data:
            food_data[item] = [((row["month"],row["year"]),[[row["price_usd"]],row["undernourishment"]])]
    for key,values in food_data.items():
        for stat in values:
            average = sum(stat[1][0]) / len(stat[1][0]) 
            stat[1][0] = average   
    return food_data


def data_filter(country,item):
    data = food_data(country)[item]
    new_data = []
    for stats in data:
        if stats[1][1] != 'No Data' :
            new_data.append(stats)
    return new_data


# index is a tuple with your first index and second index of what you want to make a list of
def listmaker(data, index):
    outp = []
    for dat in data:
        outp.append(float(dat[index[0]][index[1]]))
    return outp
 

def coeffmaker(country, item):
    return np.corrcoef(listmaker(data_filter(country,item),(1,1)), listmaker(data_filter(country,item),(1,0)))[0][1]




def get_most_product(country):
   products = pd_data.filter({'country_name':country})['item_name'].unique()
   for item in products:
        print("the coeff of "+ item + " is")
        print(coeffmaker(country, item))

get_most_product('Afghanistan')