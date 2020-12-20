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
for key in tiles:
    t = tiles[key]
    tiles_bin[key] = []
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
            s += 2**(tileSize - 1 - x)
            s_flip += 2**x
        if t[0][x] == '#':
            n += 2**x
            n_flip += 2**(tileSize - 1 - x)

    tiles_bin[key].append((n, w, s, e)) # default orientation
    tiles_bin[key].append((n_flip, e_flip, s_flip, w_flip)) # horizontal flip. vertical flip is not needed since it can be achieved through rotation
    tiles_bin[key].append((n_flip, w_flip, s_flip, e_flip)) # all coordinates inverted, use for matching only

gridSize = int(math.sqrt(len(tiles)))
unusedTiles = set((tiles.keys()))

def matchTile(sides, t1):
    for i in range(len(sides)):
        side = sides[i]
        for isFlipped in range(2):
            for j in range(len(sides)):
                side_t1 = t1[isFlipped][j]
                if side == side_t1:
                    return True
    return False

def getCornerTiles():
    keys = []
    for key in tiles_bin.keys():
        t = tiles_bin[key]
        matches = 0
        for key1 in tiles_bin:
            if key == key1:
                continue
            match = matchTile(t[0], tiles_bin[key1])
            if match != False:
                matches += 1
        if matches == 2:
            keys.append(key)
    return keys

# look for corner tile as starter
cornerTiles = getCornerTiles()
result = 1
for t in cornerTiles:
    result *= t
print("Part 1: " + str(result))
