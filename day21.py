import re

with open("input/day21", "r") as input:
    data = input.read().split("\n")
    data.pop()

allergens = {}
allIngredients = set()
foods = []

for entry in data:
    m = re.match(r"(.+) \(contains (.+)\)", entry)
    ingredient = set(m[1].split(" "))
    foods.append(ingredient) 
    allIngredients = allIngredients.union(ingredient)
    for allg in m[2].split(", "):
        if allg not in allergens:
            allergens[allg] = ingredient
        else:
            allergens[allg] = allergens[allg].intersection(ingredient)

nonAllergents = allIngredients.copy()
for key in allergens:
    nonAllergents = nonAllergents.difference(allergens[key])

numberOfNonAllergents = sum([len(nonAllergents.intersection(f)) for f in foods])

# Part 2
usedSets = set()
while sum([len(allergens[key]) for key in allergens]) != len(allergens):
    filterSet = set()
    for key in allergens:
        if len(allergens[key]) == 1 and key not in usedSets:
            filterSet = allergens[key]
            usedSets.add(key)
            break
    for key in allergens:
        if allergens[key] == filterSet:
            continue
        allergens[key] = allergens[key].difference(filterSet)

allergensSorted = list(allergens.keys())
allergensSorted.sort()

print("Part 1: " + str(numberOfNonAllergents))
print("Part 2: " + str(",".join([list(allergens[key])[0] for key in allergensSorted])))
