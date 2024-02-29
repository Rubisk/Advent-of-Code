import copy

with open("day_21.txt") as input_file:
    lines = list(input_file.readlines())
    lines = [x.replace("\n", "") for x in lines]

recipes = []
for line in lines:
    ingredients, allergies = line.split(" (")
    ingredients = ingredients.split(" ")
    allergies = allergies[9:-1].split(", ")
    recipes.append((set(ingredients), set(allergies)))


all_ingredients = set()
all_allergies = set()
for recipe in recipes:
    for ingredient in recipe[0]:
        all_ingredients.add(ingredient)
    for allergy in recipe[1]:
        all_allergies.add(allergy)

possible_ingredients = {}
for allergy in all_allergies:
    possible_ingredients[allergy] = copy.deepcopy(all_ingredients)


for ingredients, allergies in recipes:
    for allergy in allergies:
        possible_ingredients[allergy].intersection_update(ingredients)

print(possible_ingredients)

invalid_ingredients = copy.deepcopy(all_ingredients)
for ingredients in possible_ingredients.values():
    invalid_ingredients.difference_update(ingredients)


count = 0
for ingredient in invalid_ingredients:
    for recipe in recipes:
        if ingredient in recipe[0]:
            count += 1


while any([len(ingredients) > 1 for allergy, ingredients in possible_ingredients.items()]):
    for allergy, ingredients in possible_ingredients.items():
        if len(ingredients) == 1:
            for other_allergy, other_ingredients in possible_ingredients.items():
                if other_allergy != allergy:
                    other_ingredients.difference_update(ingredients)
    print(possible_ingredients)


allergy_pairs = [(allergy, ingredients.pop()) for allergy, ingredients in possible_ingredients.items()]
output = [x[1] for x in sorted(allergy_pairs)]
print(",".join(output))
