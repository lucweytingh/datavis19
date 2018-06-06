from plot import *

# pandas dataframe to be plotted
plot_df = pd_data.filter({ 'country_name': 'Niger' })

print(pd_data.filter({'item_id':65 ,'item_id': 73, 'country_name': 'Niger' }))
# any items/markets you don't want to include
blacklist = []

# run plot function
plot_by_market(plot_df, blacklist)
