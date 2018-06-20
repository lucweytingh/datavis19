from compare_regions import *

# in this question we are trying to anwser if countries in similar regions also show similar price differences

def main():
  # to awnser this we find the top correlating countries for certain items and see if they are in the same region
  correlation([0], pd_data['item_name'].unique(), 10)
  

if __name__ == "__main__":
  main()