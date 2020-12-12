with open("input/day12", "r") as input:
    data = input.read().split("\n")
    data.pop()

def move_pt1(command, val, x, y, facing):
    if command == 'N':
        y -= val
    elif command == 'W':
        x -= val
    elif command == 'E':
        x += val
    elif command == 'S':
        y += val
    elif command == 'L':
        facing += val
        if facing >= 360:
            facing -= 360
    elif command == 'R':
        facing -= val
        if facing < 0:
            facing += 360
    elif command == 'F':
        if facing == 0:
            x += val
        elif facing == 90:
            y -= val
        elif facing == 180:
            x -= val
        elif facing == 270:
            y += val
    return (x, y, facing)

def part1():
    pos = (0, 0, 0) # x, y, facing
    for entry in data:
        pos = move_pt1(entry[:1], int(entry[1:]), pos[0], pos[1], pos[2])
    return abs(pos[0]) + abs(pos[1])

def move_pt2(command, val, x, y, x_wp, y_wp):
    if command == 'N':
        y_wp -= val
    elif command == 'W':
        x_wp -= val
    elif command == 'E':
        x_wp += val
    elif command == 'S':
        y_wp += val
    elif command == 'L':

        while (val > 0):
            x_wp2 = y_wp
            y_wp2 = x_wp * -1
            x_wp = x_wp2
            y_wp = y_wp2
            val -= 90

    elif command == 'R':

        while (val > 0):
            x_wp2 = y_wp * -1
            y_wp2 = x_wp
            x_wp = x_wp2
            y_wp = y_wp2
            val -= 90

    elif command == 'F':
        x += x_wp * val
        y += y_wp * val
    return (x, y, x_wp, y_wp)

def part2():
    pos = (0, 0, 10, -1) # x, y, x_wp, y_wp
    for entry in data:
        pos = move_pt2(entry[:1], int(entry[1:]), pos[0], pos[1], pos[2], pos[3])
        print(pos)
    return abs(pos[0]) + abs(pos[1])

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))