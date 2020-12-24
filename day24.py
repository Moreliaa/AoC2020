import re

with open("input/day24", "r") as input:
    data = input.read().split("\n")
    data.pop()

tiles = {} # odd-r horizontal layout

def getNewCoords(x, y, dir):
    if dir == 'e':
        x += 1
    elif dir == 'se':
        if abs(y) % 2 != 0:
            x += 1
        y += 1
    elif dir == 'sw':
        if abs(y) % 2 == 0:
            x -= 1
        y += 1
    elif dir == 'w':
        x -= 1
    elif dir == 'nw':
        if abs(y) % 2 == 0:
            x -= 1
        y -= 1
    elif dir == 'ne':
        if abs(y) % 2 != 0:
            x += 1
        y -= 1
    return (x, y)

def flip(tile):
    if tile not in tiles:
        tiles[tile] = 0
    else:
        tiles[tile] = 1 if tiles[tile] == 0 else 0

def part1():
    for entry in data:
        matches = re.findall(r"(e|se|sw|w|nw|ne)", entry)
        coord = (0, 0)
        for m in matches:
            coord = getNewCoords(coord[0], coord[1], m)
        flip(coord)

    return list(tiles.values()).count(0)

dirs = ['e', 'se', 'sw', 'w', 'nw', 'ne']
def step(tiles_black):
    numOfAdjacentBlackTiles = {}
    for tile in tiles_black:
        if tile not in numOfAdjacentBlackTiles:
            numOfAdjacentBlackTiles[tile] = 0

        for d in dirs:
            coord = getNewCoords(tile[0], tile[1], d)
            if coord not in numOfAdjacentBlackTiles:
                numOfAdjacentBlackTiles[coord] = 1
            else:
                numOfAdjacentBlackTiles[coord] += 1

    newTiles = set()
    for key in numOfAdjacentBlackTiles:
        if key not in tiles_black and numOfAdjacentBlackTiles[key] == 2:
            newTiles.add(key)
        elif key in tiles_black and numOfAdjacentBlackTiles[key] in [1, 2]:
            newTiles.add(key)

    return newTiles

def part2():
    tiles_black = set()
    for tile in tiles:
        if tiles[tile] == 0:
            tiles_black.add(tile)

    for _ in range(100):
        tiles_black = step(tiles_black)

    return len(tiles_black)

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))