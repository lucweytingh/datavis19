from init import *

# finds the most common item in a region
def most_common_item(region_id):
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


def main():
    all_regions_dic = {}
    for region_id in pd_data['region_id'].unique():
        region = pd_data.filter({'region_id':region_id})
        item = most_common_item(region_id)
        region_dic = {}
        for index, row in region.filter({'item_name':item}).iterrows():
            if (row['month'], row['year']) not in region_dic:
                region_dic[(row['month'], row['year'])] = [row['price_usd']]
            else:
                region_dic[(row['month'], row['year'])].append(row['price_usd'])
        dates = {}
        for month, year in region_dic:
            dates[(month, year)] = sum(region_dic[(month,year)]) / len(region_dic[(month,year)])
        
        all_regions_dic[region_id] = dates
    print(all_regions_dic)





        # sum = 0
        # for price in region['price_usd']:
        #     sum += price
        # print(region_id)
        # print(sum / len(region))





if __name__ == "__main__":
    main()