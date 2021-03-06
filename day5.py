import math

with open("input/day5", "r") as input:
    data = input.read().split("\n")
    data.pop()

def parse(inputStr, idx, min, max):
    if idx == len(inputStr):
        return min

    char = inputStr[idx]
    avg = (max + min) / 2
    if char == 'F' or char == 'L':
        max = math.floor(avg)
    else: # char == 'B' or char == 'R'
        min = math.ceil(avg)
    return parse(inputStr, idx + 1, min, max)

def getSeatID(entry):
    row = parse(entry[:7], 0, 0, 127)
    col = parse(entry[7:], 0, 0, 7)
    return row * 8 + col

def getMissingSeatID(seatIDs):
    return [seatIDs[idx] + 1 for idx in range(len(seatIDs) - 1) if seatIDs[idx + 1] - seatIDs[idx] == 2][0]

seatIDs = [getSeatID(entry) for entry in data]
seatIDs.sort()

print("Part 1: " + str(seatIDs[-1]))
print("Part 2: " + str(getMissingSeatID(seatIDs)))
    
