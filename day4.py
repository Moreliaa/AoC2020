import re

with open("input/day4", "r") as input:
    data = input.read().split("\n")

reqKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optKeys = ['cid'] # why is this even here?

def isInBounds(val, min, max):
    return min <= int(val) <= max

def validateValues(passport):
    isValid = True

    for key in reqKeys:
        val = passport[key]
        if key == 'byr':
            isValid = re.match(r"^\d{4}$", val) and isInBounds(val, 1920, 2002)
        elif key == 'iyr':
            isValid = re.match(r"^\d{4}$", val) and isInBounds(val, 2010, 2020)
        elif key == 'eyr':
            isValid = re.match(r"^\d{4}$", val) and isInBounds(val, 2020, 2030)
        elif key == 'hgt':
            match = re.match(r"^(\d+)(cm|in)$", val)
            if not match:
                return False            
            isCm = match[2] == 'cm'
            min = 150 if isCm else 59
            max = 193 if isCm else 76
            isValid = isInBounds(match[1], min, max)
        elif key == 'hcl':
            isValid = re.match(r"^#[\da-f]{6}$", val)
        elif key == 'ecl':
            isValid = re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", val)
        elif key == 'pid':
            isValid = re.match(r"^\d{9}$", val)

        if not isValid:
            return False

    return True

numberOfValidPassports_pt1 = 0
numberOfValidPassports_pt2 = 0

passport = {}
for line in data:
    matches = re.findall(r"(\w+):([#\w]+)", line)
    if len(matches) == 0:
        hasRequiredKeys = True
        for key in reqKeys:
            if key not in passport:
                hasRequiredKeys = False
                break
        if hasRequiredKeys:
            numberOfValidPassports_pt1 += 1
            if validateValues(passport):
                numberOfValidPassports_pt2 += 1
        passport = {}
    else:
        for match in matches:
            passport[match[0]] = match[1]

print("Part 1: " + str(numberOfValidPassports_pt1))
print("Part 2: " + str(numberOfValidPassports_pt2))
