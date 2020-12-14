import re
import itertools

with open("input/day14", "r") as input:
    data = input.read().split("\n")
    data.pop()

ones = 0 # all bits 1 in mask set to 1
zeroes = 0 # all bits *not* 0 in mask set to 1 (including 'X')
mem = {}
for entry in data:
    match = re.match(r"mask = (.+)", entry)
    if match:
        ones = 0
        zeroes = 0
        m = match[1]
        for idx in range(len(m) - 1, -1, -1):
            c = m[idx]
            incr = 2**(len(m) - idx - 1)
            if c == 'X':
                zeroes += incr 
            elif c == '1':
                ones += incr
                zeroes += incr
    else:
        match = re.match(r"mem\[(.+)\] = (.+)", entry)
        addr =  int(match[1])
        val = int(match[2])
        mem[addr] = (val | ones) & zeroes

print("Part 1: " + str(sum(mem.values())))

all_x = 0 # all bits *not* 'X' in mask set to 1
permutations = [0]
mem = {}
for entry in data:
    match = re.match(r"mask = (.+)", entry)
    if match:
        ones = 0
        all_x = 0
        permutations = [0]
        m = match[1]
        for idx in range(len(m) - 1, -1, -1):
            c = m[idx]
            incr = 2**(len(m) - idx - 1)
            if c == 'X':
                permutations += [p + incr for p in permutations]
            elif c == '1':
                ones += incr
                all_x += incr
            elif c == '0':
                all_x += incr
    else:
        match = re.match(r"mem\[(.+)\] = (.+)", entry)
        addr =  int(match[1])
        val = int(match[2])
        addr = (addr | ones) & all_x
        for p in permutations:
            mem[addr | p] = val

print("Part 2: " + str(sum(mem.values())))