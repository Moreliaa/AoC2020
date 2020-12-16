import re

with open("input/day16", "r") as input:
    data = input.read().split("\n\n")

fields = {}
for entry in data[0].split("\n"):
    m = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", entry)
    fields[m[1]] = (int(m[2]), int(m[3]), int(m[4]), int(m[5]))

ownTicket = [int(x) for x in data[1].split("\n")[1].split(",")]

nearbyTickets = []
for entry in data[2].split("\n"):
    if entry == "nearby tickets:" or entry == "":
        continue
    nearbyTickets.append([int(x) for x in entry.split(",")])

def isValueValid(val):
    for constraints in fields.values():
        if constraints[0] <= val <= constraints[1] or constraints[2] <= val <= constraints[3]:
            return True
    return False

validTickets = [ownTicket]
def part1():
    invalid = 0
    for t in nearbyTickets:
        isTicketValid = True
        for val in t:
            if not isValueValid(val):
                invalid += val
                isTicketValid = False
        if isTicketValid:
            validTickets.append(t)
    return invalid

def removePossibleKey(possibleKeys, idx, keyToRemove):
    possibleKeys[idx].remove(keyToRemove)
    if len(possibleKeys[idx]) != 1:
        return
    keyToRemove = list(possibleKeys[idx])[0]
    for idx2 in range(len(possibleKeys)):
        if idx2 == idx or keyToRemove not in possibleKeys[idx2]:
            continue
        removePossibleKey(possibleKeys, idx2, keyToRemove)

def part2():
    possibleKeys = []
    numFields = len(ownTicket)
    for _ in range(numFields):
        possibleKeys.append(set(fields.keys()))

    for t in validTickets:
        for idx in range(numFields):
            keysToRemove = []
            for key in possibleKeys[idx]:
                constraints = fields[key]
                if not constraints[0] <= t[idx] <= constraints[1] and not constraints[2] <= t[idx] <= constraints[3]:
                    keysToRemove.append(key)
            for key in keysToRemove:
                removePossibleKey(possibleKeys, idx, key)
    
    possibleKeys = [list(keys)[0] for keys in possibleKeys]
    result = 1
    for idx in range(numFields):
        if (re.match(r"^departure", possibleKeys[idx])):
            result *= ownTicket[idx]
    return result


print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))

