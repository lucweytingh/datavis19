from init import *

# all different items and their normalisations
items = {'Bread': 'Bread', 'Wheat': 'Wheat', 'Rice (low quality)': 'Rice', 'Wage (qualified labour)': 'Wage (qualified labour)',
       'Livestock (sheep, one-year-old alive female)': 'Sheep', 'Fuel (diesel)': 'Diesel',
       'Exchange rate': 'Exchange rate', 'Wage (non-qualified labour, non-agricultural)': 'Wage (non-qualified labour)',
       'Rice': 'Rice', 'Beans (white)': 'Beans', 'Potatoes': 'Potatoes', 'Eggs': 'Eggs', 'Meat (chicken)':'Chicken',
       'Sugar':'Sugar', 'Lentils':'Lentils', 'Pasta':'Pasta', 'Tomatoes':'Tomatoes', 'Oil':'Oil', 'Cheese (dry)':'Cheese',
       'Carrots':'Carrots', 'Onions':'Onions', 'Bananas':'Bananas', 'Tea':'Tea', 'Fuel (petrol-gasoline)':'Petrol',
       'Fish (canned)':'Fish', 'Apples':'Apples', 'Milk (camel)':'Camel milk', 'Meat (camel)':'Camel',
       'Tea (sahm)':'Tea', 'Wheat flour':'Wheat flour', 'Milk': 'Milk', 'Oil (vegetable)':'Oil (vegetable)',
       'Rice (white)': 'Rice', 'Meat (pork)':'Pork', 'Meat (beef)':'Beef', 'Cabbage':'Cabbage',
       'Apples (red)':'Apples', 'Cucumbers (greenhouse)':'Cucumbers', 'Fuel (kerosene)':'Kerosene',
       'Fish (fresh)':'Fish', 'Bread (high grade flour)':'Bread',
       'Bread (first grade flour)':'Bread', 'Milk (non-pasteurized)':'Milk',
       'Rice (coarse)':'Rice', 'Lentils (masur)':'Lentils', 'Oil (palm)':'Oil (palm)', 'Rice (imported)': 'Rice',
       'Sorghum': 'Sorghum', 'Maize (white)':'Maize', 'Cassava meal (gari)':'Cassava meal', 'Maize':'Maize',
       'Millet':'Millet', 'Rice (local)':'Rice', 'Rice (imported, Indian)':'Rice',
       'Meat (beef, chops with bones)':'Beef', 'Meat (chicken, whole)':'Chicken',
       'Noodles (short)':'Noodles', 'Potatoes (Dutch)':'Potatoes', 'Potatoes (Irish, imilla)':'Potatoes',
       'Rice (estaquilla)':'Rice', 'Rice (long grain)':'Rice', 'Bread (wheat)':'Bread',
       'Rice (good quality)':'Rice', 'Rice (carolina 2da)':'Rice', 'Rice (medium grain)':'Rice',
       'Potatoes (black)':'Potatoes', 'Beans (niebe)':'Beans', 'Beans':'Beans', 'Cassava flour':'Cassava flour',
       'Sweet potatoes':'Sweet potatoes', 'Rice (imported, Tanzanian)':'Rice',
       'Rice (high quality, local)':'Rice', 'Rice (low quality, local)':'Rice',
       'Rice (mixed, low quality)':'Rice', 'Wage (non-qualified labour)':'Wage (non-qualified labour)',
       'Meat (pork, with fat)':'Pork', 'Groundnuts (shelled)':'Groundnuts', 'Sorghum (white)':'Sorghum',
       'Sesame':'Sesame', 'Peas (yellow)':'Peas', 'Soybeans':'Soybeans', 'Sorghum (red)':'Sorghum',
       'Cassava (cossette)':'Cassava', 'Groundnuts (unshelled)':'Groundnuts', 'Oil (groundnut)':'Oil (groundnut)',
       'Livestock (sheep, medium-sized castrated male)':'Sheep',
       'Livestock (goat, medium-sized castrated male)':'Goat',
       'Sorghum (berbere)':'Sorghum', 'Maize flour':'Maize flour', 'Beans (red)':'Beans', 'Garlic':'Garlic',
       'Onions (red)':'Onions', 'Onions (white)':'Onions', 'Maize (yellow)': 'Maize', 'Plantains':'Plantains',
       'Cocoa':'Cocoa', 'Coffee':'Coffee', 'Fish (dry)':'Fish', 'Salt':'Salt', 'Rice (paddy)':'Rice',
       'Chickpeas (imported)':'Chickpeas', 'Eggs (white, AA)':'Eggs', 'Meat (beef, minced)':'Beef',
       'Peas (green, dry)':'Peas', 'Potatoes (unica)':'Potatoes', 'Sugar (brown)':'Sugar (brown)',
       'Sugar (brown, loaf)':'Sugar (brown)', 'Cauliflower':'Cauliflower', 'Oranges (big size)':'Oranges',
       'Beans (red, fresh)':'Beans', 'Cassava (dry)':'Cassava', 'Spinach':'Spinach', 'Fish (tilapia)':'Fish',
       'Beans (string)':'Beans', 'Guava':'Guava', 'Papaya':'Papaya', 'Blackberry':'Blackberry', 'Broccoli':'Broccoli',
       'Mangoes':'Mangoes', 'Pumpkin':'Pumpkin', 'Tamarillos/tree tomatoes':'Tomatoes', 'Cheese':'Cheese',
       'Lentils (imported)':'Lentils', 'Milk (pasteurized)':'Milk', 'Coffee (instant)':'Coffee',
       'Oil (sunflower)':'Oil (sunflower)', 'Meat (chicken, frozen)':'Chicken', 'Cassava (fresh)':'Cassava',
       'Fish (smoked)':'Fish', 'Fish (salted)':'Fish', 'Groundnuts (paste)':'Groundnuts',
       'Beans (black)':'Beans', 'Rice (milled 80-20)':'Rice',
       'Rice (denikassia, imported)':'Rice', 'Yam (florido)':'Yam', 'Cornstarch':'Cornstarch',
       'Fish (appolo)':'Fish', 'Peanut':'Peanut', 'Groundnuts':'Groundnuts', 'Cashew':'Cashew', 'Cotton':'Cotton',
       'Maize meal':'Maize meal', 'Cassava':'Cassava', 'Meat (goat, with bones)':'Goat',
       'Cassava (chikwangue)':'Cassava', 'Transport (public)':'Public transport', 'Beans (silk red)':'Beans',
       'Livestock (Goat)':'Goat', 'Livestock (Sheep)':'Sheep', 'Beans (fava, dry)':'Beans',
       'Maize (local)':'Maize', 'Rice (long grain, imported)':'Rice',
       'Rice (medium grain, imported)':'Rice', 'Rice (small grain, imported)':'Rice',
       'Fonio':'Fonio', 'Rice (paddy, long grain, local)':'Rice',
       'Rice (basmati, broken)':'Rice', 'Potatoes (Irish)':'Potatoes', 'Fish (bonga)':'Fish',
       'Meat (mutton)':'Lamb', 'Milk (powder)':'Milk (powder)', 'Beans (dry)':'Beans',
       'Plantains (apentu)':'Plantains', 'Yam':'Yam', 'Rice (ordinary, second quality)':'Rice',
       'Tortilla (maize)':'Tortilla', 'Rice (ordinary, first quality)':'Rice',
       'Oil (vegetable, imported)':'Oil (vegetable)', 'Fish':'Fish', 'Tomatoes (paste)':'Tomatoes',
       'Beans (niebe, white)':'Beans', 'Cassava meal (attieke)':'Cassava', 'Rice (tchako)':'Rice',
       'Wheat flour (imported)':'Wheat flour', 'Sugar (white)':'Sugar', 'Maize meal (local)':'Maize meal',
       'Maize flour (white)':'Maize flour', 'Tea (black)':'Tea', 'Oil (mustard)':'Oil (mustard)',
       'Oil (soybean)':'Oil (soybean)', 'Lentils (moong)':'Lentils', 'Sugar (jaggery/gur)':'Sugar',
       'Lentils (urad)':'Lentils', 'Ghee (vanaspati)':'Ghee', 'Salt (iodised)':'Salt',
       'Meat (chicken, broiler)':'Chicken', 'Chili (green)':'Chili (green)', 'Chili (red)': 'Chili (red)',
       'Milk (condensed)': 'Milk', 'Bread (khoboz)':'Bread', 'Pulses':'Pulses', 'Oil (olive)':'Oil (olive)',
       'Chickpeas': 'Chickpeas', 'Bulgur':'Bulgur', 'Cheese (picon)':'Cheese', 'Fish (tuna, canned)':'Tuna',
       'Bread (pita)':'Bread', 'Meat (lamb)':'Lamb', 'Cheese (white, boiled)':'Cheese',
       'Cucumbers':'Cucumbers', 'Milk (cow, pasteurized)':'Milk', 'Oil (cotton)':'Oil (cotton)',
       'Tea (green)': 'Tea', 'Wheat flour (first grade)':'Wheat flour',
       'Wheat flour (high quality)':'Wheat flour', 'Beans (kidney white)':'Beans',
       'Meat (beef, first quality)':'Beef', 'Meat (beef, second quality)':'Beef',
       'Meat (buffalo, first quality)':'Buffalo', 'Meat (buffalo, second quality)':'Buffalo',
       'Meat (pork, first quality)':'Pork', 'Meat (pork, second quality)':'Pork',
       'Rice (glutinous, first quality)':'Rice',
       'Rice (glutinous, second quality)':'Rice', 'Rice (glutinous, unmilled)':'Rice',
       'Rice (ordinary, unmilled)':'Rice', 'Garlic (small)':'Garlic', 'Fish (snake head)':'Snake head',
       'Fish (catfish)':'Catfish', 'Fish (tilapia, farmed)':'Tilapia',
       'Rice (imported, Egyptian)':'Rice', 'Lettuce':'Lettuce', 'Meat (beef, canned)':'Beef',
       'Fish (sardine, canned)':'Sardine', 'Bread (brown)':'Bread', 'Peas (split, dry)':'Peas',
       'Beans (sugar-red)':'Beans', 'Cowpeas':'Cowpeas', 'Rice (white, imported)':'Rice',
       'Wage (non-qualified labour, agricultural)':'Wage (non-qualified labour)', 'Sorghum (taghalit)':'Sorghum',
       'Wheat flour (local)':'Wheat flour', 'Maize meal (white, first grade)': 'Maize meal',
       'Oil (vegetable, local)': 'Oil (vegetable)', 'Sugar (brown, imported)': 'Sugar (brown)',
       'Sugar (brown, local)': 'Sugar (brown)', 'Groundnuts (Mix)':'Groundnuts', 'Beans (butter)':'Beans',
       'Groundnuts (large, shelled)':'Groundnuts', 'Groundnuts (small, shelled)':'Groundnuts',
       'Beans (catarino)':'Catarino', 'Maize meal (white, without bran) ':' Maize meal',
       'Beans (magnum)':'Beans', 'Maize meal (white, with bran)':'Maize meal',
       'Rice (high quality)':'Rice', 'Chickpeas (local)':'Chickpeas', 'Oil (mixed, imported)':'Oil (mixed)',
       'Cowpeas (white)':'Cowpeas (white)', 'Cowpeas (brown)':'Cowpeas (brown)', 'Sorghum (brown)':'Sorghum',
       'Gari (yellow)':'Gari (yellow)', 'Gari (white)':'Gari (white)', 'Yam (Abuja)': 'Yam', 'Oil (cooking)': 'Oil (cooking)',
       'Ghee (artificial)':'Ghee', 'Poultry': 'Poultry', 'Beans(mash)':'Beans',
       'Wheat flour (locally processed)':'Wheat flour', 'Rice (regular, milled)':'Rice',
       'Beans (mung)':'Beans', 'Maize flour (imported)':'Maize flour', 'Sorghum flour':'Sorghum flour',
       'Peppers (green)':'Peppers (green)', 'Eggplants':'Eggplants', 'Charcoal':'Charcoal', 'Passion fruit':'Passion fruit',
       'Zucchini':'Zucchini', 'Livestock (hen)':'Hen', 'Avocados':'Avocados', 'Cassava leaves':'Cassava leaves',
       'Peas (fresh)':'Peas', 'Peas (dry)':'Peas', 'Livestock (cattle)':'Cow',
       'Livestock (pig)':'Pig', 'Meat (goat)':'Goat', 'Beans (green, fresh)':'Beans',
       'Maize (imported)':'Maize', 'Rice (red nadu)':'Rice', 'Beans (sugar) ':'Beans',
       'Bread (bakery)':'Bread', 'Bread (shop)':'Bread', 'Dates':'Dates', 'Fuel (gas)':'Gas',
       'Livestock (sheep, two-year-old male)':'Sheep', 'Yogurt':'Yoghurt', 'Parsley':'Parsley',
       'Beans (haricot)':'Beans', 'Beans (kidney)':'Beans', 'Eggs (imported)':'Eggs',
       'Meat (chicken, imported)':'Chicken', 'Bread (common)':'Bread', 'Oranges':'Oranges',
       'Meat (veal)':'Veal', 'Milk (powder, infant formula)':'Milk', 'Cocoa (powder)':'Cocoa',
       'Electricity':'Electricity', 'Tea (herbal)':'Tea', 'Water':'Water', 'Curd':'Curd', 'Sour cream':'Sour cream',
       'Meat (mixed, sausage)':'Sausage', 'Beetroots':'Beetroots', 'Butter':'Butter', 'Buckwheat grits':'Buckwheat grits',
       'Bread (rye)':'Bread', 'Fat (salo)':'Salo', 'Beans (kidney red)':'Beans',
       'Peas (yellow, split)':'Peas', 'Cassava meal':'Cassava meal',
       'Maize meal (white, roller)':'Maize meal', 'Maize meal (white, breakfast)':'Maize meal',
       'Oil (vegetable, fortified)':'Oil (vegetable)', 'Maize meal (white, fortified)':'Maize meal',
       'Wheat flour (fortified)':'Wheat flour', 'Sugar (white, fortified)':'Sugar',
       'Bananas (medium size)':'Bananas', 'Fish (red snapper)':'Fish',
       'Onions (dry, local)':'Onions', 'Potatoes (medium size)':'Potatoes',
       'Tomatoes (greenhouse)':'Tomatoes', 'Oil (maize)':'Oil (maize)', 'Labaneh':'Labeneh', 'Cheese (goat)':'Cheese',
       'Fish (frozen)':'Fish', 'Water (drinking)':'Water', 'Sorghum (food aid)':'Sorghum',
       'Ghee (natural)':'Ghee', 'Oil (mixed)':'Oil (mixed)', 'Meat (beef, without bones)':'Beef',
       'Exchange rate (unofficial)':'Exchange rate', 'Millet (white)':'Millet'}

def normalize_items(items):
    norm_items = []
    # iterate through rows in data
    for index, row in pd_data.iterrows():
        norm_items.append(items[row['item_name']])
    
    # save to a new file
    pd_data['item_name'] = norm_items
    pd_data.to_csv('norm_data.csv', encoding='utf-8', index=False)

normalize_items(items)