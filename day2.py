import re

with open("input/day2", "r") as input:
    data = input.read().split("\n")

data.pop()

def extractData(inputStr): 
    match = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", inputStr)
    min = int(match[1])
    max = int(match[2])
    targetChar = match[3]
    pw = match[4]
    return tuple((min, max, targetChar, pw))

data = [extractData(entry) for entry in data]

numberOfValidPws_pt1 = 0
numberOfValidPws_pt2 = 0

for entry in data:
    min = entry[0]
    max = entry[1]
    targetChar = entry[2]
    pw = entry[3]
    count = 0

    for char in pw:
        if char == targetChar:
            count += 1
            if count > max:
                break

    if count >= min and count <= max:
        numberOfValidPws_pt1 += 1

    if (pw[min - 1] == targetChar) != (pw[max - 1] == targetChar):
        numberOfValidPws_pt2 += 1

print("Part 1: " + str(numberOfValidPws_pt1))
print("Part 2: " + str(numberOfValidPws_pt2))