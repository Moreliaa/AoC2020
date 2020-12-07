from collections import namedtuple
import re

with open("input/day7", "r") as input:
    data = input.read().split("\n")
    data.pop()

Bag = namedtuple('Bag', ['count', 'color'])

bags = {}
for entry in data:
    entry = entry.split(" bags contain ")
    matches = [re.match(r"^(\d+) (.+) bags?\.?$", bag) for bag in entry[1].split(", ")]
    bags[entry[0]] = [Bag(int(match[1]) , match[2]) for match in matches if match]

def traverse(bag, targetBag):
    for containedBag in bag:
        if containedBag.color == targetBag or traverse(bags[containedBag.color], targetBag):
            return True
    return False

def traverseCount(bag):
    return sum([containedBag.count + containedBag.count * traverseCount(bags[containedBag.color]) for containedBag in bag])

pt1_bags = [color for color in bags if traverse(bags[color], "shiny gold")]

print("Part 1: " + str(len(pt1_bags)))
print("Part 2: " + str(traverseCount(bags["shiny gold"])))
    