with open("input/day6", "r") as input:
    data = input.read().split("\n")

sum_pt1 = 0
sum_pt2 = 0

answers = {}
numInGroup = 0
for entry in data:
    if len(entry) == 0:
        sum_pt1 += len(answers)
        sum_pt2 += len([char for char in answers if answers[char] == numInGroup])

        answers = {}
        numInGroup = 0
        continue

    numInGroup += 1
    for char in entry:
        if char not in answers:
            answers[char] = 1
        else:
            answers[char] += 1

print("Part 1: " + str(sum_pt1))
print("Part 2: " + str(sum_pt2))