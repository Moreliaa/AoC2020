from collections import deque

input = "716892543"
cups = [deque([int(c)]) for c in input]
cups_dict = {}

def move(curr):
    c_rm = []
    last = curr[1]
    for _ in range(3):
        c_rm.append(last)
        last = last[1]
    curr[1] = last 
    
    c_min = 1
    while cups_dict[c_min] == curr or cups_dict[c_min] in c_rm:
        c_min += 1
    c_max = len(cups)
    while cups_dict[c_max] == curr or cups_dict[c_max] in c_rm:
        c_max -= 1

    dest = curr[0] - 1 
    while (dest == 0 or cups_dict[dest] in c_rm or cups_dict[dest] == curr):
        dest = dest - 1 if dest > c_min else c_max
    
    destNext = cups_dict[dest][1]
    cups_dict[dest][1] = c_rm[0]
    c_rm[-1][1] = destNext
    return curr[1]


for i in range(len(cups)):
    cups_dict[cups[i][0]] = cups[i]
    if i > 0:
        cups[i - 1].append(cups[i])
cups[-1].append(cups[0])

curr = cups[0]
for _ in range(100):
    curr = move(curr)
    
result = ""
curr = cups_dict[1]
for i in range(len(cups)):
    result += str(curr[1][0])
    curr = curr[1]
print("Part 1: " + result)

cups = [deque([int(c)]) for c in input]
for i in range(10, 1000001):
    cups.append(deque([i]))
cups_dict = {}
for i in range(len(cups)):
    cups_dict[cups[i][0]] = cups[i]
    if i > 0:
        cups[i - 1].append(cups[i])
cups[-1].append(cups[0])

curr = cups[0]
for _ in range(10000000):
    curr = move(curr)

values = cups_dict[1][1]

print("Part 2: " + str(values[0] * values[1][0]))