with open("input/day10", "r") as input:
    data = input.read().split("\n")
    data.pop()
    data = [int(entry) for entry in data]

data.sort()
data = [0] + data + [data[-1] + 3]

def part1():
    num1 = 0
    num3 = 0

    for idx in range(1, len(data)):
        if idx == 0:
            res = data[idx]
        else:
            res = data[idx] - data[idx - 1]

        if (res == 1):
            num1 += 1
        elif (res == 3):
            num3 += 1
    
    return num1 * num3

nodeCache = {}
def getNextNodes(currentIdx):
    if (currentIdx not in nodeCache):
        nodeCache[currentIdx] = [idx for idx in range(currentIdx, len(data)) if 1 <= data[idx] - data[currentIdx] <= 3]
    return nodeCache[currentIdx]

edgeCache = {}
edgeCache[len(data) - 1] = 1

def countEdges(idx):
    if (idx in edgeCache):
        return edgeCache[idx]

    total = 0
    nextNodes = getNextNodes(idx)
    for node in nextNodes:
        total += countEdges(node)
    edgeCache[idx] = total
    return total

print("Part 1: " + str(part1()))
print("Part 2: " + str(countEdges(0)))
