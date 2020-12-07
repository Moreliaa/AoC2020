import re

with open("input/day7", "r") as input:
    data = input.read().split("\n")
    data.pop()

bags = {}
for entry in data:
    entry = entry.split(" bags contain ")
    matches = [re.match(r"^(\d+) (.+) bags?\.?$", bag) for bag in entry[1].split(", ")]
    bags[entry[0]] = [(match[1] , match[2]) for match in matches if match]

def traverse(bag, targetBag):
    for containedBag in bag:
        nextBag = containedBag[1]
        if nextBag == targetBag or traverse(bags[nextBag], targetBag):
            return True
    return False

def traverseCount(bag):
    return sum([int(containedBag[0]) + int(containedBag[0]) * traverseCount(bags[containedBag[1]]) for containedBag in bag])

pt1_bags = [color for color in bags if traverse(bags[color], "shiny gold")]

print("Part 1: " + str(len(pt1_bags)))
print("Part 2: " + str(traverseCount(bags["shiny gold"])))
    