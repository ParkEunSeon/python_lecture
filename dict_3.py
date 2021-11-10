foods = ['떡볶이','짜장면','라면','피자','맥주','치킨']

foods = {"떡볶이":"오뎅",
         "짜장면":"단무지",
         "라면":"김치",
         "피자":"피클",
         "맥주":"땅콩",
         "치킨":"치킨무",
         "삼겹살":"상추",};
food_list = list(foods)
side_list = list(foods.values())
dict_food = list(zip(foods.keys(),foods.values()))
print(dict_food)
