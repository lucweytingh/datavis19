dic_region_id = {'Afghanistan': 1, 'Algeria': 2, 'Armenia': 3, 'Azerbaijan': 3, 'Bangladesh': 1,
       'Benin': 4, 'Bhutan': 1, 'Bolivia': 5, 'Burkina Faso': 4, 'Burundi': 4, 'Cambodia': 6,
       'Cameroon': 4, 'Cape Verde': 4, 'Central African Republic': 4, 'Chad': 4,
       'Colombia': 5, 'Congo': 4, 'Costa Rica': 5, "Cote d'Ivoire": 4,
       'Democratic Republic of the Congo': 4, 'Djibouti': 2, 'El Salvador': 5,
       'Ethiopia': 4, 'Gambia': 4, 'Georgia':3, 'Ghana':4, 'Guatemala':5,
       'Guinea-Bissau':4, 'Guinea':4, 'Haiti':5, 'Honduras':5, 'India':1,
       'Indonesia':6, 'Iran  (Islamic Republic of)':2, 'Iraq':2, 'Jordan':2,
       'Kenya':4, 'Kyrgyzstan':3, "Lao People's Democratic Republic":6,
       'Lebanon':2, 'Lesotho':4, 'Liberia':4, 'Madagascar':4, 'Malawi':4, 'Mali':4,
       'Mauritania':4, 'Mozambique':4, 'Myanmar':6, 'Nepal':1, 'Niger':4, 'Nigeria':4,
       'Pakistan':1, 'Panama':5, 'Peru':5, 'Philippines':6, 'Rwanda':4, 'Senegal':4,
       'Sri Lanka': 1, 'Swaziland':4, 'Syrian Arab Republic':2, 'Tajikistan':3,
       'Timor-Leste':6, 'Turkey':3, 'Uganda':4, 'Ukraine':3,
       'United Republic of Tanzania':4, 'Yemen':2, 'Zambia':4, 'Zimbabwe':4,
       'State of Palestine':2, 'Sudan':4, 'Egypt':2, 'South Sudan':4}


dic_id_name = {1: "South Asia", 2:"Middle East & North Africa", 3:"Europe & Central Asia",
            4:"Sub-Saharan Africa", 5:"Latin America & Caribbean", 6:"East Asia & Pacific"}


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
