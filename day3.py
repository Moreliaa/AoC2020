with open("input/day3", "r") as input:
    data = input.read().split("\n")
    data.pop()

def getTile(idx, slope_x, slope_y):
    entry = data[idx]
    x = (slope_x / slope_y) * idx
    x_int = int(x)
    if x_int != 0 and x / x_int != 1:
        return '.'
    return entry[(x_int % len(entry))]

def runSlope(slope_x, slope_y):
    return [getTile(idx, slope_x, slope_y) for idx in range(len(data))].count('#')

def part1():    
    print("Part 1: " + str(runSlope(3,1)))

def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    numberOfTrees = [runSlope(slope[0], slope[1]) for slope in slopes]
    result = numberOfTrees[0]
    for idx in range(1, len(numberOfTrees)):
        result *= numberOfTrees[idx]
    print("Part 2: " + str(result))

part1()
part2()