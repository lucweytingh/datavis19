from compare_regions import *

# in this question we are trying to anwser if countries in similar regions also show similar price differences

def main():
  # to awnser this we find the top correlating countries for certain items and see if they are in the same region
  correlation([0], pd_data['item_name'].unique(), 10)
  

# find the items both countries have
def shared_items(country1,country2):
  items_c1 = pd_data.filter({'country_name' : country1})["item_name"].unique()
  items_c2 = pd_data.filter({'country_name' : country2})["item_name"].unique()
  return [x for x in items_c1 if x in items_c2]

# returns shared years, starting month and end month of certain item
def shared_months(country1,country2, item):
  # find all shared years for item
    years_c1 = pd_data.filter({'item_name': item, 'country_name': country1})['year'].unique()
    years_c2 = pd_data.filter({'item_name': item, 'country_name': country2})['year'].unique()
    sharedyears = [x for x in years_c1 if x in years_c2]

    # find shared start month in first year
    months_c1 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[0]})['month'].unique()
    months_c2 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[0]})['month'].unique()
    sharedmonths = [x for x in months_c1 if x in months_c2]
    month_s = sharedmonths[0]

    # find shared last month in last year
    months_c1 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[-1]})['month'].unique()
    months_c2 = pd_data.filter({'item_name': item, 'country_name': country1, 'year':sharedyears[-1]})['month'].unique()
    sharedmonths = [x for x in months_c1 if x in months_c2]
    month_e = sharedmonths[-1]
    return sharedyears, month_s, month_e

