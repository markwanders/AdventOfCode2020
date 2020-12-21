import re

with open("input.txt") as f:
    foods = f.read().splitlines()

all_ingredients = set()
allergens_in_food = dict()
for food in foods:
    ingredients, allergens = map(lambda x: x.replace(",", "").split(" "), food.rstrip(")").split(" (contains "))
    all_ingredients.update(ingredients)
    for allergen in allergens:
        if allergen in allergens_in_food:
            allergens_in_food[allergen].append(ingredients)
        else:
            allergens_in_food[allergen] = [ingredients]
contains_allergens = set()
for allergen, list_of_food in allergens_in_food.items():
    contains_allergens |= set.intersection(*map(set, list_of_food))
ingredients_without_allergens = [i for i in all_ingredients if i not in contains_allergens]
count = 0
for ingredient in ingredients_without_allergens:
    for food in foods:
        pattern = fr"(?:^| )({ingredient})(?:$| )"
        count = count + 1 if re.search(pattern, food) else count
print(count)

possible_ingredients = dict()
for allergen, possible_foods in allergens_in_food.items():
    possible_ingredients[allergen] = set.intersection(*map(set, possible_foods))

actual_ingredients = dict()
while len(actual_ingredients.keys()) < len(possible_ingredients.keys()):
    for allergen, possible_ingredient in possible_ingredients.items():
        if allergen not in actual_ingredients.keys() and len(possible_ingredient) == 1:
            actual_ingredients[allergen] = possible_ingredient.pop()
            for a, p_i in possible_ingredients.items():
                if a != allergen and actual_ingredients[allergen] in p_i:
                    p_i.remove(actual_ingredients[allergen])
print(",".join(list(dict(sorted(actual_ingredients.items())).values())))
