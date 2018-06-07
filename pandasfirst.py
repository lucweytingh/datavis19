from init import *

print(pd_data)


def datefinder(country):
    

def makenormcolumn():
    normlist = []
    countries = pd_data['country_name'].unique()
    
    for country in countries:
        country_data = pd_data.filter({'country_name':country})
        currency = country_data['cur_name'].unique()[0]

        #currency_list = currency_list_maker(currency,dates)
        





makenormcolumn()