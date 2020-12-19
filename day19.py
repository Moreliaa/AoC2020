import re

with open("input/day19", "r") as input:
    data = input.read().split("\n\n")
    data = [entry.split("\n") for entry in data]
    data[1].pop()

d = {}
for entry in data[0]:
    m = re.match(r"(\d+): (.+)", entry)
    d[m[1]] = [e.split(' ') for e in m[2].split(' | ')]

def checkRule(key, msg, startIdx):
    rules = d[key]
    for r in rules:
        idx = startIdx
        result = True
        for num in r:
            if num[0] == '"':
                if msg[idx] != num[1]:
                    result = False
                    break
            elif not checkRule(num, msg, idx):
                result = False
                break
            idx += 1
        if result:
            return result
    return False

print([checkRule("0", msg, 0) for msg in data[1]].count(True))