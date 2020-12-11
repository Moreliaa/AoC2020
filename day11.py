with open("input/day11", "r") as input:
    data = input.read().split("\n")
    data.pop()

slopes_yx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # NW N NE W E SW S SE
seatsInLos = []
def getSeatsInLos():
    for lineIdx in range(len(data)):
        line = []
        for charIdx in range(len(data[lineIdx])):
            coords = []
            if data[lineIdx][charIdx] == 'L':
                coords.append((lineIdx, charIdx))
                for slope in slopes_yx:
                    y = lineIdx + slope[0]
                    x = charIdx + slope[1]
                    while 0 <= y < len(data) and 0 <= x < len(data[lineIdx]):
                        if (data[y][x] == 'L'):
                            coords.append((y, x))
                            break
                        y += slope[0]
                        x += slope[1]

            line.append(coords)

        seatsInLos.append(line)

def getNumOccupiedSeats_pt1(lineIdx, charIdx, state):
    min_y = lineIdx - 1 if lineIdx > 0 else 0
    min_x = charIdx - 1 if charIdx > 0 else 0
    max_y = lineIdx + 2 if lineIdx < len(state) - 1 else len(state)
    max_x = charIdx + 2 if charIdx < len(state[lineIdx]) - 1 else len(state[lineIdx])
    return [state[y][x] for y in range(min_y, max_y) for x in range(min_x, max_x)].count('#')

def getNumOccupiedSeats_pt2(lineIdx, charIdx, state):
    return sum([1 for (y, x) in seatsInLos[lineIdx][charIdx] if state[y][x] == '#'])

def applyRules(lineIdx, state, isPt1):    
    line = ''
    for charIdx in range(len(state[lineIdx])):
        char = state[lineIdx][charIdx]
        if char == '.':
            line += char
        else:
            numOccupiedSeats = getNumOccupiedSeats_pt1(lineIdx, charIdx, state) if isPt1 else getNumOccupiedSeats_pt2(lineIdx, charIdx, state)
            maxOccupiedAllowed = 5 if isPt1 else 6

            if char == 'L' and numOccupiedSeats == 0:
                line += '#'
            elif char == '#' and numOccupiedSeats >= maxOccupiedAllowed:
                line += 'L'
            else:
                line += char
    return line

def progress(lastState, isPt1):
    nextState = []
    stabilized = True
    for idx in range(len(lastState)):
        nextState.append(applyRules(idx, lastState, isPt1))
        if nextState[idx] != lastState[idx]:
            stabilized = False
    return (nextState, stabilized)

def parts(isPt1):
    state = (data, False)
    while not state[1]:
        state = progress(state[0], isPt1)
    return sum([line.count('#') for line in state[0]])

getSeatsInLos()
print("Part 1: " + str(parts(True)))
print("Part 2: " + str(parts(False)))
