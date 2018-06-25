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
       'Beans (catarino)':'Catarino', 'Maize meal (white, without bran) ':'Maize meal',
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

items_data = [(281, 'Tea'), (414, 'Cheese'), (442, 'Milk (powder, infant formula)'), (304, 'Transport (public)'), (62, 'Oil (palm)'), (179, 'Wheat flour (local)'), (372, 'Butter'), (105, 'Garlic'), (292, 'Peppers (green)'), (432, 'Beans (sugar) '), (51, 'Maize'), (482, 'Gari (yellow)'), (112, 'Pasta'), (117, 'Rice (paddy, long grain, local)'), (390, 'Livestock (Sheep)'), (152, 'Fish (bonga)'), (99, 'Yam'), (408, 'Papaya'), (433, 'Meat (veal)'), (122, 'Rice (basmati, broken)'), (479, 'Cowpeas (white)'), (65, 'Sorghum'), (320, 'Meat (beef, canned)'), (386, 'Meat (lamb)'), (184, 'Oil (sunflower)'), (251, 'Rice (imported, Indian)'), (56, 'Maize (local)'), (434, 'Eggplants'), (447, 'Passion fruit'), (114, 'Tomatoes'), (364, 'Yogurt'), (488, 'Cotton'), (243, 'Tomatoes (greenhouse)'), (172, 'Oil (cotton)'), (458, 'Beans (green, fresh)'), (264, 'Maize meal (white, roller)'), (78, 'Beans (red)'), (54, 'Maize meal'), (282, 'Sorghum (red)'), (64, 'Rice (imported)'), (136, 'Maize (yellow)'), (415, 'Lentils (imported)'), (97, 'Sugar'), (139, 'Fish'), (258, 'Bulgur'), (102, 'Milk (non-pasteurized)'), (393, 'Beans (mung)'), (494, 'Oil (vegetable, fortified)'), (73, 'Millet'), (163, 'Pulses'), (119, 'Groundnuts (shelled)'), (332, 'Lentils (urad)'), (322, 'Fish (tuna, canned)'), (468, 'Meat (beef, without bones)'), (231, 'Cauliflower'), (156, 'Sesame'), (344, 'Meat (camel)'), (126, 'Noodles (short)'), (68, 'Cassava'), (383, 'Livestock (Goat)'), (478, 'Sorghum (berbere)'), (306, 'Oil (soybean)'), (363, 'Labaneh'), (146, 'Millet (white)'), (70, 'Rice (denikassia, imported)'), (128, 'Potatoes (Irish, imilla)'), (230, 'Bananas (medium size)'), (173, 'Onions'), (67, 'Maize (white)'), (130, 'Rice (estaquilla)'), (203, 'Rice (paddy)'), (181, 'Cabbage'), (268, 'Beans (red, fresh)'), (351, 'Groundnuts (paste)'), (360, 'Oranges'), (424, 'Peas (yellow, split)'), (141, 'Meat (beef)'), (165, 'Rice (mixed, low quality)'), (319, 'Cheese (picon)'), (289, 'Garlic (small)'), (229, 'Apples (red)'), (127, 'Potatoes (Dutch)'), (189, 'Meat (buffalo, first quality)'), (253, 'Sorghum flour'), (369, 'Meat (mixed, sausage)'), (373, 'Buckwheat grits'), (120, 'Beans (niebe)'), (368, 'Sour cream'), (418, 'Beans (butter)'), (208, 'Chickpeas (imported)'), (192, 'Meat (pork, first quality)'), (245, 'Oil (groundnut)'), (223, 'Sugar (brown, imported)'), (374, 'Bread (rye)'), (217, 'Cassava meal'), (158, 'Maize (imported)'), (133, 'Rice (white)'), (384, 'Bread (pita)'), (311, 'Fish (tilapia, farmed)'), (176, 'Tea (green)'), (406, 'Beans (string)'), (401, 'Fish (fresh)'), (285, 'Fuel (petrol-gasoline)'), (316, 'Rice (imported, Egyptian)'), (247, 'Rice (high quality)'), (233, 'Cucumbers (greenhouse)'), (238, 'Milk (powder)'), (90, 'Chili (green)'), (138, 'Poultry'), (455, 'Cassava leaves'), (248, 'Soybeans'), (137, 'Oil'), (211, 'Meat (beef, minced)'), (313, 'Dates'), (403, 'Cassava meal (gari)'), (151, 'Coffee'), (413, 'Tamarillos/tree tomatoes'), (249, 'Sorghum (food aid)'), (214, 'Sugar (brown)'), (134, 'Maize flour (white)'), (206, 'Beans (kidney red)'), (71, 'Rice (local)'), (175, 'Tea (black)'), (299, 'Meat (chicken, imported)'), (450, 'Zucchini'), (242, 'Potatoes (medium size)'), (490, 'Beans (niebe, white)'), (503, 'Cassava meal (attieke)'), (185, 'Salt'), (101, 'Oil (vegetable, imported)'), (410, 'Broccoli'), (227, 'Rice (small grain, imported)'), (405, 'Fish (tilapia)'), (170, 'Fish (appolo)'), (94, 'Meat (chicken)'), (239, 'Oil (olive)'), (91, 'Chili (red)'), (325, 'Lentils (moong)'), (87, 'Sweet potatoes'), (197, 'Rice (ordinary, first quality)'), (178, 'Wheat flour (high quality)'), (222, 'Oil (vegetable, local)'), (394, 'Chickpeas (local)'), (329, 'Meat (pork, with fat)'), (460, 'Bread (first grade flour)'), (123, 'Meat (beef, chops with bones)'), (129, 'Rice (carolina 2da)'), (72, 'Yam (florido)'), (309, 'Fish (snake head)'), (407, 'Guava'), (318, 'Lettuce'), (436, 'Rice (good quality)'), (131, 'Rice (medium grain)'), (354, 'Beans (sugar-red)'), (476, 'Livestock (sheep, medium-sized castrated male)'), (426, 'Rice (low quality, local)'), (76, 'Maize flour'), (187, 'Meat (beef, first quality)'), (200, 'Sorghum (taghalit)'), (366, 'Wheat flour (locally processed)'), (489, 'Water (drinking)'), (298, 'Eggs (imported)'), (381, 'Rice (imported, Tanzanian)'), (331, 'Sugar (jaggery/gur)'), (124, 'Bread (common)'), (303, 'Cassava (chikwangue)'), (355, 'Groundnuts (Mix)'), (493, 'Water'), (300, 'Fish (smoked)'), (195, 'Rice (glutinous, second quality)'), (280, 'Bread (shop)'), (305, 'Exchange rate'), (213, 'Potatoes (unica)'), (100, 'Fonio'), (57, 'Rice (tchako)'), (82, 'Oil (cooking)'), (265, 'Maize meal (white, breakfast)'), (463, 'Milk (pasteurized)'), (135, 'Sorghum (white)'), (98, 'Plantains (apentu)'), (199, 'Rice (ordinary, unmilled)'), (343, 'Fish (canned)'), (274, 'Wage (qualified labour)'), (209, 'Coffee (instant)'), (396, 'Oil (mixed, imported)'), (480, 'Cowpeas (brown)'), (236, 'Meat (goat, with bones)'), (481, 'Sorghum (brown)'), (456, 'Peas (fresh)'), (269, 'Tortilla (maize)'), (85, 'Beans (black)'), (241, 'Oranges (big size)'), (457, 'Peas (dry)'), (365, 'Cheese (goat)'), (169, 'Cornstarch'), (422, 'Livestock (pig)'), (198, 'Rice (ordinary, second quality)'), (186, 'Peas (yellow)'), (404, 'Spinach'), (210, 'Eggs (white, AA)'), (125, 'Meat (chicken, whole)'), (162, 'Rice (long grain)'), (502, 'Cocoa (powder)'), (66, 'Beans (white)'), (395, 'Oil (mixed)'), (473, 'Exchange rate (unofficial)'), (80, 'Rice (regular, milled)'), (147, 'Plantains'), (345, 'Apples'), (286, 'Maize meal (white, with bran)'), (459, 'Bread (high grade flour)'), (215, 'Sugar (brown, loaf)'), (96, 'Oil (vegetable)'), (166, 'Carrots'), (454, 'Avocados'), (157, 'Rice (red nadu)'), (254, 'Bananas'), (357, 'Tea (sahm)'), (453, 'Livestock (hen)'), (301, 'Fish (salted)'), (477, 'Livestock (goat, medium-sized castrated male)'), (259, 'Bread (khoboz)'), (108, 'Lentils'), (361, 'Livestock (sheep, two-year-old male)'), (107, 'Ghee (natural)'), (77, 'Maize flour (imported)'), (234, 'Fish (red snapper)'), (333, 'Ghee (vanaspati)'), (334, 'Salt (iodised)'), (278, 'Bread (bakery)'), (140, 'Meat (pork)'), (171, 'Fish (dry)'), (483, 'Gari (white)'), (60, 'Rice (coarse)'), (118, 'Groundnuts (unshelled)'), (409, 'Blackberry'), (388, 'Cucumbers'), (55, 'Bread'), (317, 'Tomatoes (paste)'), (196, 'Rice (glutinous, unmilled)'), (392, 'Beans (haricot)'), (491, 'Electricity'), (411, 'Mangoes'), (425, 'Rice (high quality, local)'), (226, 'Rice (medium grain, imported)'), (188, 'Meat (beef, second quality)'), (92, 'Eggs'), (497, 'Sugar (white, fortified)'), (89, 'Meat (chicken, broiler)'), (484, 'Yam (Abuja)'), (159, 'Bread (brown)'), (58, 'Wheat flour'), (225, 'Rice (long grain, imported)'), (218, 'Cowpeas'), (370, 'Beetroots'), (110, 'Onions (red)'), (106, 'Ghee (artificial)'), (84, 'Wheat'), (387, 'Cheese (white, boiled)'), (161, 'Peas (split, dry)'), (111, 'Onions (white)'), (174, 'Peanut'), (412, 'Pumpkin'), (310, 'Fish (catfish)'), (302, 'Cassava (cossette)'), (83, 'Potatoes'), (228, 'Oil (mustard)'), (419, 'Beans (magnum)'), (287, 'Livestock (cattle)'), (362, 'Oil (maize)'), (153, 'Groundnuts'), (277, 'Wage (non-qualified labour)'), (142, 'Cheese (dry)'), (224, 'Sugar (brown, local)'), (61, 'Lentils (masur)'), (341, 'Fuel (gas)'), (150, 'Cocoa'), (420, 'Groundnuts (large, shelled)'), (367, 'Curd'), (52, 'Rice'), (183, 'Meat (mutton)'), (427, 'Beans (catarino)'), (400, 'Rice (white, imported)'), (385, 'Beans (fava, dry)'), (376, 'Fat (salo)'), (81, 'Milk'), (167, 'Cashew'), (221, 'Maize meal (white, first grade)'), (431, 'Maize meal (white, without bran) '), (50, 'Beans'), (86, 'Rice (milled 80-20)'), (240, 'Onions (dry, local)'), (291, 'Cassava (fresh)'), (180, 'Beans (kidney)'), (446, 'Charcoal'), (212, 'Peas (green, dry)'), (194, 'Rice (glutinous, first quality)'), (290, 'Cassava (dry)'), (144, 'Potatoes (black)'), (79, 'Beans (silk red)'), (262, 'Beans (dry)'), (326, 'Beans(mash)'), (469, 'Parsley'), (284, 'Fuel (diesel)'), (190, 'Meat (buffalo, second quality)'), (471, 'Maize meal (local)'), (467, 'Wage (non-qualified labour, agricultural)'), (486, 'Fish (frozen)'), (465, 'Wage (non-qualified labour, non-agricultural)'), (495, 'Maize meal (white, fortified)'), (451, 'Meat (goat)'), (342, 'Milk (camel)'), (375, 'Bread (wheat)'), (472, 'Milk (cow, pasteurized)'), (74, 'Cassava flour'), (95, 'Milk (condensed)'), (207, 'Meat (chicken, frozen)'), (148, 'Potatoes (Irish)'), (244, 'Chickpeas'), (177, 'Wheat flour (first grade)'), (492, 'Tea (herbal)'), (421, 'Groundnuts (small, shelled)'), (349, 'Sugar (white)'), (389, 'Beans (kidney white)'), (145, 'Rice (low quality)'), (496, 'Wheat flour (fortified)'), (283, 'Fuel (kerosene)'), (339, 'Wheat flour (imported)'), (321, 'Fish (sardine, canned)'), (275, 'Livestock (sheep, one-year-old alive female)'), (193, 'Meat (pork, second quality)')]

def get_item_id(item_name):
  try:
    id = [t for t in items_data if t[1] == item_name][0][0]
  except IndexError:
    id = None
  return id

def normalize_items(pd_data, items):
  norm_items = []
  norm_ids = []
  # iterate through rows in data
  for index, row in pd_data.iterrows():
    new_item_name = items[row['item_name']]
    norm_items.append(new_item_name)
    new_item_id = get_item_id(new_item_name) or get_item_id(row['item_name'])
    norm_ids.append(new_item_id)

  # save to dataframe
  pd_data['item_id'] = norm_ids
  pd_data['item_name'] = norm_items

if __name__ == "__main__":
  import os
  import sys
  sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
  from datavis19.init import *
  normalize_items(pd_data, items)
  pd_data.to_csv('data/data_item_norm.csv', encoding='utf-8', index=False)
