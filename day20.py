import re
import math

with open("input/day20", "r") as input:
    data = input.read().split("\n\n")
    data = [entry.split("\n") for entry in data]
    data.pop()

tiles = {}
for entry in data:
    match = re.match(r"Tile (\d+):", entry[0])
    tiles[int(match[1])] = entry[1:]

tileSize = 10 # hardcoded laziness
tiles_bin = {}
for coord in tiles:
    t = tiles[coord]
    tiles_bin[coord] = []
    n, w, s, e = 0, 0, 0, 0 # bitwise edges with lowest bit on the right for n
    n_flip, w_flip, s_flip, e_flip = 0, 0, 0, 0
    for y in range(tileSize):
        if t[y][0] == '#':
            w += 2**y
            w_flip += 2**(tileSize - 1 - y)
        if t[y][tileSize - 1] == '#': 
            e += 2**(tileSize - 1 - y)
            e_flip += 2**y
    for x in range(tileSize):
        if t[tileSize - 1][x] == '#':
            s += 2**x
            s_flip += 2**(tileSize - 1 - x) 
        if t[0][x] == '#':
            n += 2**(tileSize - 1 - x)
            n_flip += 2**x

    tiles_bin[coord].append((n, w, s, e)) # default orientation
    tiles_bin[coord].append((n_flip, e_flip, s_flip, w_flip)) # horizontal flip. vertical flip is not needed since it can be achieved through rotation
    tiles_bin[coord].append((n_flip, w_flip, s_flip, e_flip)) # all coordinates inverted, use for matching only
    tiles_bin[coord].append((n, e, s, w)) # horizontal flip, all coordinates inverted, use for matching only

gridSize = int(math.sqrt(len(tiles)))

def matchTile(sides, t1):
    for i in range(len(sides)):
        side = sides[i]
        for j in range(2, 4):
            for k in range(len(sides)):
                side_t1 = t1[j][k]
                if side == side_t1:
                    return (i, j, k) # i: index of the side of sides that was matched, j == 3 if t1 is flipped otherwise j == 2, k == index of side of t1 that was matched 
    return False

unusedTiles = set((tiles.keys()))
tiles_arranged = {}
tiles_orientation = {}
def getCornerTiles():
    keys = []
    for key in tiles_bin.keys():
        t = tiles_bin[key]
        matches = []
        kak = []
        for key1 in tiles_bin:
            if key == key1:
                continue
            match = matchTile(t[0], tiles_bin[key1])
            if match != False:
                matches.append(match)
                kak.append(key1)
        if len(matches) == 2:
            keys.append(key)
            if 2 <= matches[0][0] <= 3 and 2 <= matches[1][0] <= 3: # pick a tile for which S and E sides were matched as top left corner
                tiles_arranged[(0, 0)] = t[0]
                tiles_orientation[(0, 0)] = (key, False, 0)
    unusedTiles.remove(tiles_orientation[(0, 0)][0]) 
    return keys

# look for corner tile as starter
cornerTiles = getCornerTiles()
result = 1
for t in cornerTiles:
    result *= t

print("Part 1: " + str(result))

# Part 2
def buildGrid(currentCoord):
    coords = [(currentCoord[0], currentCoord[1] - 1), (currentCoord[0] - 1, currentCoord[1]), (currentCoord[0], currentCoord[1] + 1), (currentCoord[0] + 1, currentCoord[1])]
    nextCoords = []
    for coordIdx in range(len(coords)):
        coord = coords[coordIdx]
        if coord in tiles_arranged:
            continue

        for key1 in unusedTiles:
            match = matchTile(tiles_arranged[currentCoord], tiles_bin[key1])
            if match != False and match[0] == coordIdx:
                rotation = 0 # positive rotation is clockwise
                diff = match[0] - match[2]
                while diff != -2 and diff != 2: # rotate t1 appropriately
                    if (diff < -2):
                        rotation += 1
                        diff += 1
                    else:
                        rotation -= 1
                        diff -= 1
                if rotation < 0:
                    rotation += 4
                
                isFlipped = match[1] == 3
                sides1Old = tiles_bin[key1][match[1] - 2]
                sides1New = tuple([sides1Old[(idx + rotation) % len(sides1Old)] for idx in range(len(sides1Old))])
                tiles_arranged[coord] = sides1New
                tiles_orientation[coord] = (key1, isFlipped, rotation)
                unusedTiles.remove(key1)
                nextCoords.append(coord)
                break
    
    for coord in nextCoords:
        buildGrid(coord)

buildGrid((0, 0))

tiles_adjusted = {}
for coord in tiles_orientation:
    tileInfo = tiles_orientation[coord]
    tile = tiles[tileInfo[0]]
    newTile = []
    for i in range(1, 9):
        newTile.append(tile[i][1:9])
    if tileInfo[1]: # flipped
        for i in range(len(newTile)):
            newTile[i] = newTile[i][::-1]

    rotation = tileInfo[2]
    while (rotation > 0):
        newTile = [[newTile[y][x] for y in range(len(newTile))] for x in range(len(newTile[0]))] # transpose
        newTile = [newTile[y][::-1] for y in range(len(newTile))]
        rotation -= 1
    tiles_adjusted[coord] = newTile

asciiGrid = []
for y in range(gridSize):
    for x in range(gridSize):
        tile = tiles_adjusted[(x, y)]
        for yStart in range(len(tile)):
            yGrid = len(tile) * y + yStart
            if len(asciiGrid) == yGrid:
                asciiGrid.append([])
            asciiGrid[yGrid] += tile[yStart]

for y in range(len(asciiGrid)):
    asciiGrid[y] = "".join(asciiGrid[y])

print(asciiGrid)

seaMonster = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...']
seaMonsterIdx = []
for y in range(len(seaMonster)):
    seaMonsterIdx.append([])
    for x in range(len(seaMonster[0])):
        if seaMonster[y][x] == '#':
            seaMonsterIdx[y].append(x)


def isSeaMonster(y, x):
    for y_s in range(len(seaMonsterIdx)):
        for x_s in seaMonsterIdx[y_s]:
            if asciiGrid[y + y_s][x + x_s] != '#':
                return False
    return True

monstersFound = 0
iterations = 0
while monstersFound == 0 and iterations < 8:
    for y in range(len(asciiGrid) - len(seaMonster)):
        for x in range(len(asciiGrid) - len(seaMonster[0])):
            if isSeaMonster(y, x):
                monstersFound += 1
    asciiGrid = [[asciiGrid[y][x] for y in range(len(asciiGrid))] for x in range(len(asciiGrid[0]))] # transpose
    asciiGrid = [asciiGrid[y][::-1] for y in range(len(asciiGrid))]
    for y in range(len(asciiGrid)):
        asciiGrid[y] = "".join(asciiGrid[y])
    iterations += 1
    if iterations == 4:
        for y in range(len(asciiGrid)): # flip
            asciiGrid[y] = asciiGrid[y][::-1]
    

print(monstersFound)
numHash = sum([1 for y in range(len(asciiGrid)) for x in range(len(asciiGrid)) if asciiGrid[y][x] == '#'])
monsterSize = sum([len(y) for y in seaMonsterIdx])
print("Part 2: " + str(numHash - monstersFound * monsterSize))