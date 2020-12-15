start = (8, 11, 0, 19, 1, 2)

def parts(targetIdx):
    mem = {}
    idx = 1
    for n in start:
        mem[n] = (idx, idx)
        lastNum = n
        idx += 1

    while idx <= targetIdx:
        nextNum = mem[lastNum][0] - mem[lastNum][1]
        mem[nextNum] = (idx, mem[nextNum][0]) if nextNum in mem else (idx, idx)
        
        lastNum = nextNum
        idx += 1

    return str(lastNum)

print("Part 1: " + parts(2020))
print("Part 2: " + parts(30000000))