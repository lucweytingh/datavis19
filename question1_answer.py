# Are there any food prices that are show negative/positive correlation, and is this correlation present throughout the years, or perhaps only in certain period? Can you perhaps detect possible ingredients of a certain other food product?

from init import *
from plot import *

# - There is a number of ‘perfect’ correlations (r = 1.0 or -1.0). All of these are very simple, mostly straight lines, which we attribute to a lack of data. It could be that these products correlate (and often, the items are related - e.g., two types of fish, or oil) but the data is so invariant that this doesn’t tell anything significant.
# - Interesting positive correlations with related products:
#     - Tajikistan, Gharm, lamb and beef, C: 0.999 [beef is slightly cheaper than lamb but they both follow a rather volatile price over time]
#         - Also prevalent in: Tajikistan, Dushanbe; Kyrgyzstan, Osh;
#     - Syrian Arab Republic, Jableh, sugar and beans, C: 0.998 [they both increase, then start dropping in the start of 2017. Beans data is missing from before 2017, and only shows a straight increasing line]
#     - South Sudan, Rumbek, sorghum and maize, C: 0.996 [similar products, very similar price, pretty stable with a huge spike halfway through 2016]
#         - Similarity between sorghum and maize also prevalent in other countries
#     - Mozambique, Beira, beans and catarino, C: 0.996 [catarino is a type of bean, these follow the same price almost entirely]
#     - South Sudan, Kuajok, groundnuts and sesame, C: 0.994 [once again, very similar price, large spike in 2016]
#     - Guatemala, national average, bananas and plantains, C: 0.993 [plaintains are cooking bananas, these prices are super similar]
#     - white cowpeas are cheaper than brown cowpeas in Nigeria, Gombe
#     - Syrian Arab Republic, lentils and tea, C: 0.992 [these products follow the same trends, except for the fact that tea became way more expensive in 2015 while lentils stayed the same]

# - Positive correlations with product pairs of hyper- and hyponyms (ingredients):
#     - Diesel and petrol often have a high correlation, since they are closely related products. Examples:
#         - Yemen, Marib City, C: 0.996
#     - In Ukraine, milk, sour cream, curd, and butter are closely correlated in markets through the country. Examples include:
#         - Ukraine, National Average, sour cream and milk, C: 0.998
#         - Ukraine, Zhytomyr, sour cream and curd, C: 0.997 [not ingredients of each other but they have a common ingredient (milk)]
#         - Ukraine, Kiev, butter and milk, C: 0.997
#     - DRotC, Mwene-Ditu, maize meal and maize, C: 0.997
#         - Also prevalent in: DRotC, Mbuji-may

# - Negative correlations with related products:
#     - Lao PDR, Borikhamxay, C: -0.964, snake head and tilapia [these are both fish]
#     - India, T.Puram, C: -0.907, oil (sunflower) and rice [small but definite negative correlation, interesting because these products seem unrelated]


# Top 10 positive correlations sorted by sum of correlations:
# ('Sorghum', 'Maize'), sum: 232.46, avg: 0.58
# ('Beans', 'Maize'), sum: 219.48, avg: 0.47
# ('Rice', 'Maize'), sum: 217.42, avg: 0.38
# ('Beans', 'Rice'), sum: 181.37, avg: 0.44
# ('Sorghum', 'Millet'), sum: 150.13, avg: 0.70
# ('Petrol', 'Diesel'), sum: 125.83, avg: 0.80
# ('Groundnuts', 'Beans'), sum: 124.79, avg: 0.52
# ('Groundnuts', 'Maize'), sum: 123.91, avg: 0.47
# ('Groundnuts', 'Rice'), sum: 113.46, avg: 0.56
# ('Maize', 'Millet'), sum: 109.34, avg: 0.57
# ('Wheat flour', 'Rice'), sum: 85.58, avg: 0.34

# Top 10 positive correlations sorted by average of correlations:
# ('Oil (maize)', 'Oil (sunflower)'), sum: 1.00, avg: 1.00
# ('Oil (sunflower)', 'Oil (mixed)'), sum: 1.00, avg: 1.00
# ('Pasta', 'Oil (mixed)'), sum: 1.00, avg: 1.00
# ('Oil (maize)', 'Oil (mixed)'), sum: 0.99, avg: 0.99
# ('Wheat flour', 'Oil (mixed)'), sum: 0.99, avg: 0.99
# ('Pasta', 'Oil (sunflower)'), sum: 0.99, avg: 0.99
# ('Cheese', 'Plantains'), sum: 0.99, avg: 0.99
# ('Milk', 'Sour cream'), sum: 25.64, avg: 0.99
# ('Sour cream', 'Butter'), sum: 25.55, avg: 0.98
# ('Milk', 'Butter'), sum: 25.49, avg: 0.98
# ('Curd', 'Sour cream'), sum: 25.47, avg: 0.98

# Top 10 negative correlations sorted by sum of correlations:
# ('Potatoes', 'Bananas'), sum: -20.55, avg: -0.26
# ('Lentils', 'Milk (powder)'), sum: -19.63, avg: -0.56
# ('Sorghum', 'Bananas'), sum: -19.09, avg: -0.29
# ('Cassava leaves', 'Cassava flour'), sum: -18.90, avg: -0.43
# ('Bananas', 'Sorghum flour'), sum: -18.68, avg: -0.31
# ('Peppers (green)', 'Bananas'), sum: -17.48, avg: -0.29
# ('Soybeans', 'Tomatoes'), sum: -17.10, avg: -0.30
# ('Sugar', 'Onions'), sum: -16.72, avg: -0.17
# ('Maize', 'Tomatoes'), sum: -16.46, avg: -0.25
# ('Carrots', 'Soybeans'), sum: -15.45, avg: -0.27
# ('Eggplants', 'Bananas'), sum: -15.22, avg: -0.25

# Top 10 negative correlations sorted by average of correlations:
# ('Lentils', 'Sorghum'), sum: -0.95, avg: -0.95
# ('Wage (non-qualified labour)', 'Groundnuts'), sum: -0.90, avg: -0.90
# ('Pig', 'Cucumbers'), sum: -0.79, avg: -0.79
# ('Oil (cooking)', 'Beans'), sum: -3.80, avg: -0.76
# ('Veal', 'Potatoes'), sum: -0.75, avg: -0.75
# ('Cocoa', 'Groundnuts'), sum: -0.74, avg: -0.74
# ('Oil (cooking)', 'Sugar'), sum: -3.65, avg: -0.73
# ('Groundnuts', 'Plantains'), sum: -0.72, avg: -0.72
# ('Cassava', 'Sugar (brown)'), sum: -0.70, avg: -0.70
# ('Sugar (brown)', 'Fish'), sum: -0.69, avg: -0.69
# ('Sheep', 'Milk'), sum: -1.38, avg: -0.69
