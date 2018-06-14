from init import *

# finds the most common item in a region or overall
def most_common_item(region_id=None):
    if region_id == None:
        region = pd_data
    else:
        region = pd_data.filter({'region_id':region_id})
    options = region['item_name'].unique()
    result_count = 0
    result_item = ""
    for item in options:
        attempt = len(region.filter({'item_name':item})['country_name'].unique())
        if attempt > result_count:
            result_count = attempt
            result_item = item
    return result_item


def compare(region_id = None, item = None):
    all_dic = {}
    if item == None:
        item = most_common_item(region_id)
    if region_id == None:
        evaluate_name = 'region_name'
    else:
        evaluate_name = 'country_name'
    for data_item in pd_data[evaluate_name].unique():
        data = pd_data.filter({evaluate_name:data_item})
        data_dic = {}
        for index, row in data.filter({'item_name':item}).iterrows():
            if (row['month'], row['year']) not in data_dic:
                data_dic[(row['month'], row['year'])] = [row['price_usd']]
            else:
                data_dic[(row['month'], row['year'])].append(row['price_usd'])
        average = {}
        for month, year in data_dic:
            average[(month, year)] = sum(data_dic[(month,year)]) / len(data_dic[(month,year)])
        all_dic[data_item] = average
    return all_dic


def main():
    print(compare())


if __name__ == "__main__":
    main()