from itertools import product

with open("input/day17", "r") as input:
    data = input.read().split("\n")
    data.pop()

def parseInput(dimensions):
    field = set()
    for idx in range(len(data)):
        line = data[idx]
        for idx2 in range(len(line)):
            if line[idx2] == '#':                
                field.add(tuple([idx2, idx] + [0 for _ in range(dimensions - 2)]))
    return field

def parts(dimensions):
    field = parseInput(dimensions)
    permutations = set(product(range(-1, 2), repeat=dimensions))
    permutations.remove(tuple([0 for i in range(dimensions)]))

    for _ in range(6):
        numOfActiveNeighbours = {}
        for pos in field:
            for p in permutations:
                affectedPos = tuple([pos[i] + p[i] for i in range(dimensions)])
                if affectedPos not in numOfActiveNeighbours:
                    numOfActiveNeighbours[affectedPos] = 1
                else:
                    numOfActiveNeighbours[affectedPos] += 1

        nextField = set()
        for pos in numOfActiveNeighbours:
            val = numOfActiveNeighbours[pos]
            if (pos in field and val == 2) or val == 3:
                nextField.add(pos)
        field = nextField

    return str(len(field))

print("Part 1: " + parts(3))
print("Part 2: " + parts(4))
