from init import *
df = pd.read_csv('../exchange.csv')

dates = ["2017-03","2017-04","2017-05","2017-06"]
currency = "AFN"
stattype = "Average of observations through period"




def currency_dictionary_maker(currency,stattype,dates):
    dict = {}
    months = df.filter({'CURRENCY': currency, "Collection": stattype, 'Frequency': 'Monthly'})
    for date in dates:
        dict[date] = months[date].unique()[0]
    print(dict)

currency_dictionary_maker(currency,stattype,dates)
