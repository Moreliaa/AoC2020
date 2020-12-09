with open("input/day8", "r") as input:
    data = input.read().split("\n")
    data.pop()

def part1():
    acc = 0
    idx = 0
    cache = {}

    while True:
        if idx in cache:
            break

        entry = data[idx].split(" ")
        cache[idx] = (entry[0], int(entry[1]))

        if cache[idx][0] == "acc":
            acc += cache[idx][1]
            idx += 1
        elif cache[idx][0] == "jmp":
            idx += cache[idx][1]
        else: #nop
            idx += 1
    
    return acc

def part2():
    idxNextChange = 0
    while idxNextChange < len(data):
        acc = 0
        idx = 0
        idxInstructionsPassed = 0
        cache = {}

        while True:
            if idx in cache or idx >= len(data):
                idxNextChange += 1
                break

            entry = data[idx].split(" ")
            cache[idx] = (entry[0], int(entry[1]))

            if cache[idx][0] == "acc":
                acc += cache[idx][1]
                idx += 1
            elif cache[idx][0] == "jmp":
                if idxNextChange == idxInstructionsPassed:
                    idx += 1
                else:
                    idx += cache[idx][1]
                idxInstructionsPassed += 1
            else: #nop
                if idxNextChange == idxInstructionsPassed:
                    idx += cache[idx][1]
                else:
                    idx += 1
                idxInstructionsPassed += 1
        
        if idx == len(data):
            break
    
    return acc

        
print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))
