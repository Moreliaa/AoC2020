with open("input/day9", "r") as input:
    data = input.read().split("\n")
    data.pop()
    data = [int(entry) for entry in data]

def checkPreamble(list, number):
    for n in list:
        if number - n in list:
            return True
    return False

def part1():
    for idx in range(25, len(data)):
        if not checkPreamble(data[idx-25:idx], data[idx]):
            return data[idx]

invalid = part1()

idxStart = 0
idxEnd = 0
acc = 0

while idxStart < len(data):
    if acc == invalid:
        break
    elif acc < invalid:
        acc += data[idxEnd]
        idxEnd += 1
    else:
        while acc > invalid and idxEnd > idxStart:
            acc -= data[idxStart]
            idxStart += 1

pt2_sorted = data[idxStart:idxEnd]
pt2_sorted.sort()

print("Part 1: " + str(invalid))
print("Part 2: " + str(pt2_sorted[0] + pt2_sorted[-1]))