import re

with open("input/day19", "r") as input:
    data = input.read().split("\n\n")
    data = [entry.split("\n") for entry in data]
    data[1].pop()

d = {}
for entry in data[0]:
    m = re.match(r"(\d+): (.+)", entry)
    d[m[1]] = [e.split(' ') for e in m[2].split(' | ')]

def buildHugeRegex(key, isPt2):
    rules = d[key]
    regex = "("
    for idx in range(len(rules)):
        r = rules[idx]
        for num in r:
            if num[0] == '"':
                regex += num[1]
            else:
                regex += buildHugeRegex(num, isPt2)
        if idx != len(rules) - 1:
            regex += "|"
    regex += ")"        
    if isPt2 and key == '8':
        regex += '+'
    return regex

def parts(isPt2):
    rx = '^' + buildHugeRegex("0", isPt2) + '$'
    matches = [re.match(rx, msg) for msg in data[1]]
    return str(len(matches) - matches.count(None))

print("Part 1: " + parts(False))

# Part 2
for i in range(2, 20): # arbitrary upper limit of 20, might need more depending on input
    rule = []
    for j in range(i):
        rule.append('42')
    for k in range(i):
        rule.append('31')
    d['11'].append(rule)

print("Part 2: " + parts(True))