dic_region_id = {'Afghanistan': 1, 'Algeria': 2, 'Armenia': 3, 'Azerbaijan': 3, 'Bangladesh': 4,
       'Benin': 5, 'Bhutan': 4, 'Bolivia': 6, 'Burkina Faso': 5, 'Burundi': 5, 'Cambodia': 7,
       'Cameroon': 5, 'Cape Verde': 5, 'Central African Republic': 5, 'Chad': 5,
       'Colombia': 6, 'Congo': 5, 'Costa Rica': 6, "Cote d'Ivoire": 5,
       'Democratic Republic of the Congo': 5, 'Djibouti': 2, 'El Salvador': 6,
       'Ethiopia': 5, 'Gambia': 5, 'Georgia':3, 'Ghana':5, 'Guatemala':6,
       'Guinea-Bissau':5, 'Guinea':5, 'Haiti':6, 'Honduras':6, 'India':4,
       'Indonesia':7, 'Iran  (Islamic Republic of)':2, 'Iraq':2, 'Jordan':2,
       'Kenya':5, 'Kyrgyzstan':3, "Lao People's Democratic Republic":7,
       'Lebanon':2, 'Lesotho':5, 'Liberia':5, 'Madagascar':5, 'Malawi':5, 'Mali':5,
       'Mauritania':5, 'Mozambique':5, 'Myanmar':7, 'Nepal':1, 'Niger':5, 'Nigeria':5,
       'Pakistan':1, 'Panama':6, 'Peru':6, 'Philippines':7, 'Rwanda':5, 'Senegal':5,
       'Sri Lanka': 1, 'Swaziland':5, 'Syrian Arab Republic':2, 'Tajikistan':3,
       'Timor-Leste':7, 'Turkey':3, 'Uganda':5, 'Ukraine':3,
       'United Republic of Tanzania':5, 'Yemen':2, 'Zambia':5, 'Zimbabwe':5,
       'State of Palestine':2, 'Sudan':5, 'Egypt':2, 'South Sudan':5}


dic_id_name = {1: "South Asia", 2:"Middle East & North Africa", 3:"Europe & Central Asia",
        4:"South Asia", 5:"Sub-Saharan Africa", 6:"Latin America & Caribbean", 7:"East Asia & Pacific"}


def addregions(pd_data, dic_region_id, dic_id_name):
    region_id = []
    region_name = []
    for country, region in dic_region_id.items():
        amount = pd_data.filter({'country_name':country})['country_id'].count()
        addregion_id, addregion_name = [], []

        for i in range(amount):
            addregion_id.append(region)
            addregion_name.append(dic_id_name[region])
        region_id = region_id + addregion_id
        region_name = region_name + addregion_name

    pd_data['region_id'] = region_id
    pd_data['region_name'] = region_name

if __name__ == "__main__":
  import os
  import sys
  sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
  from datavis19.init import *
  addregions(pd_data, dic_region_id, dic_id_name)
  pd_data.to_csv('data/data_region.csv', encoding='utf-8', index=False)
