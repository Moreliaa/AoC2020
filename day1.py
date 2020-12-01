with open("input/day1", "r") as input:
    data = input.read().split("\n")

data.pop()
data = [int(entry) for entry in data]

def part1():
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            v1 = data[i]
            v2 = data[j]
            if v1 + v2 == 2020:
                print("Part 1: " + str(v1 * v2))
                return

def part2():
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            v1 = data[i]
            v2 = data[j]
            if v1 + v2 <= 2020:
                for k in range(len(data)):
                    if k == i or k == j:
                        continue
                    v3 = data[k]
                    if v1 + v2 + v3 == 2020:
                        print("Part 2: " + str(v1 * v2 * v3))
                        return

part1()
part2()