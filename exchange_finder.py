from init import *

df = pd.read_csv('../exchange.csv')

def currency_dictionary_maker(currency,stattype,dates):
    dict = {}
    months = df.filter({'CURRENCY': currency, "Collection": stattype, 'Frequency': 'Monthly'})
    for date in dates:
        dict[date] = months[date].unique()[0]
    print(dict)


