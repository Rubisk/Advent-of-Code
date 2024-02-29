import copy
import itertools as it
import math


class Ingredient(object):
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

    def __repr__(self):
        return "{0} (x{1})".format(self.type, self.quantity)


reactions = {}
types = set(["ORE"])

with open("input_14.txt") as file:
    for line in file.readlines():
        input_ingredients = []
        line = line.replace(",", "")
        line = line.replace("\n", "")
        input_ingredient_strings = line.split(" ")[:-3]
        while len(input_ingredient_strings) > 0:
            type = input_ingredient_strings[1]
            quantity = int(input_ingredient_strings[0])
            input_ingredients.append(Ingredient(type, quantity))
            input_ingredient_strings = input_ingredient_strings[2:]

        output_ingredient_string = line.split(" ")[-2:]
        type = output_ingredient_string[1]
        quantity = int(output_ingredient_string[0])
        output_ingredient = Ingredient(type, quantity)
        reactions[output_ingredient.type] = (output_ingredient, input_ingredients)
        types.add(output_ingredient.type)


def find_ore_required(fuel_quantity):
    required = [Ingredient(type, 0) if type != "FUEL" else Ingredient(type, fuel_quantity) for type in types]
    should_continue = True
    while should_continue:
        should_continue = False
        for needed_ingredient in required:
            if needed_ingredient.type == "ORE" or needed_ingredient.quantity <= 0:
                continue
            should_continue = True
            output, inputs = reactions[needed_ingredient.type]
            times_to_run = math.ceil(needed_ingredient.quantity / output.quantity)
            leftover = output.quantity * times_to_run - needed_ingredient.quantity
            needed_ingredient.quantity = -leftover

            for input in inputs:
                done = False
                for ingredient in required:
                    if ingredient.type == input.type:
                        ingredient.quantity += times_to_run * input.quantity
                        done = True
                if not done:
                    print(input.type)
    for ingredient in required:
        if ingredient.type == "ORE":
            return ingredient.quantity

max_fuel = 1000000000000

upper_bound = 1
while find_ore_required(upper_bound) < max_fuel:
    upper_bound *= 2
lower_bound = int(upper_bound / 2)

print(upper_bound, lower_bound)

while lower_bound < upper_bound:
    middle = int(upper_bound + lower_bound) / 2
    if find_ore_required(middle) < max_fuel:
        lower_bound = middle
    else:
        upper_bound = middle - 1
    print(upper_bound, lower_bound)




