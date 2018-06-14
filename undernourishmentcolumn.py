from init import *


exceptions = {'Congo' : 'Democratic Republic of the Congo', 'Bhutan': 'South Asia', 'Burundi':'South Asia', 'Timor-Leste': 'Timor', 'Sudan': 'Middle East & North Africa', 'South Sudan': 'Middle East & North Africa', 'Syrian Arab Republic': 'Middle East & North Africa'}

nodata = ['Ukraine', 'State of Palestine']

def makeundercolumn(pd_data, und_data):
    outp = []
    countries = pd_data['country_name'].unique()
    for country in countries:
        print(country)
        search_country = country
        if country in exceptions.keys():
            search_country = exceptions[country]
        print(search_country)
        nourishlist = []
        country_pd = pd_data.filter({'country_name':country})
        country_und = und_data.filter({"Entity":search_country})
        years_list = country_pd["year"].tolist()
        for year in years_list:
            if year > 2015 or year < 1991 or country in nodata:
                nourishlist.append("No Data")
            else:
                nourishlist.append(country_und.filter({"Year":year})["POU"].tolist()[0])
        outp.extend(nourishlist)
    with open("newcolumn.txt", "w") as f:
        for s in outp:
            f.write(str(s) +"\n")
    pd_data['undernourishment'] = outp  



if __name__ == "__main__":
  makeundercolumn(pd_data,und_data)
  pd_data.to_csv('data/data_undernourishment.csv', encoding='utf-8', index=False)