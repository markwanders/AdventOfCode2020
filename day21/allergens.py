import re

with open("input.txt") as f:
    foods = f.read().splitlines()

all_ingredients = set()
all_foods = set()
allergens_in_food = dict()
for food in foods:
    ingredients, allergens = map(
        lambda x: x.replace("(", "").replace(")", "").replace("contains ", "").replace(",", "").split(" "),
        food.split(" ("))
    all_ingredients.update(ingredients)
    all_foods.add(" ".join(ingredients))
    for allergen in allergens:
        if allergen in allergens_in_food.keys():
            allergens_in_food[allergen].append(ingredients)
        else:
            allergens_in_food[allergen] = [ingredients]
contains_allergens = set()
for allergen, list_of_food in allergens_in_food.items():
    contains_allergens.update(set.intersection(*map(set, list_of_food)))
ingredients_without_allergens = [i for i in all_ingredients if i not in contains_allergens]
count = 0
for ingredient in ingredients_without_allergens:
    for food in all_foods:
        pattern = fr"(?:^| )({ingredient})(?:$| )"
        matches = re.findall(pattern, food)
        count += len(matches)
print(count)
