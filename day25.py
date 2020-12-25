with open("input/day25", "r") as input:
    data = input.read().split("\n")
    data.pop()
data = [int(entry) for entry in data]

def transform(sub, lSize):
    val = 1
    for _ in range(lSize):
        val = (val * sub) % 20201227
    return val

p1, p2 = data[0], data[1]
size = 1
val = 1
s1, s2 = 0, 0
while s1 == 0 or s2 == 0:
    val = (val * 7) % 20201227
    if val == p1:
        s1 = size
        print(s1)
    if val == p2:
        s2 = size
        print(s2)
    size += 1

print("Part 1: " + str(transform(p1, s2)) + " | " + str(transform(p2, s1)))