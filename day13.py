import math

with open("input/day13", "r") as input:
    data = input.read().split("\n")

def lcm(a, b):
    return int(abs(a * b) / math.gcd(a, b))

t0 = int(data[0])
busIDs = [int(entry) for entry in data[1].split(',') if entry != 'x']

t1 = {}
minID = busIDs[0]
for ID in busIDs:
    t1[ID] = t0 + (ID - t0 % ID)
    if t1[ID] < t1[minID]:
        minID = ID

print("Part 1: " + str((t1[minID] - t0) * minID))

t_offset = {}
offset = 0
for entry in data[1].split(','):
    if entry != 'x':
        t_offset[int(entry)] = offset
    offset += 1

t = 0
increment = busIDs[0]
for ID in busIDs:
    while (t + t_offset[ID]) % ID != 0:
        t += increment
    increment = lcm(increment, ID)

print("Part 2: " + str(t))