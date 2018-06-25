from init import *

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

exceptions = {'Congo' : 'Democratic Republic of the Congo', 'Bhutan': 'South Asia', 'Burundi':'South Asia', 'Timor-Leste': 'Timor', 'Sudan': 'Middle East & North Africa', 'South Sudan': 'Middle East & North Africa', 'Syrian Arab Republic': 'Middle East & North Africa'}
result = []
for index,row in und_data.iterrows():  
    if row["Entity"] in dic_region_id:
        result.append(dic_region_id[row["Entity"]])
    elif row["Entity"] in exceptions:
        country = exceptions[row["Entity"]]
        result.append(dic_region_id[country])
    else:
        result.append("No Data")
print(result)
und_data["region"] = result
und_data.to_csv('data/prevalence-of-undernourishment.csv', encoding='utf-8', index=False)

