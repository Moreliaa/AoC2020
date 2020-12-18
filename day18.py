with open("input/day18", "r") as input:
    data = input.read().split("\n")
    data.pop()

def handleOp(acc, val, op):
    if op == '+':
        return acc + val
    elif op == '*':
        return acc * val
    else:
        raise "op"

def calculate_pt1(line, i):
    acc = 0
    val = ''
    op = '+'
    
    while i < len(line):
        c = line[i]

        if c == ' ':
            if val != '':
                acc = handleOp(acc, int(val), op)
                val = ''
        elif c == '+' or c == '*':
            op = c
            i += 1
        elif "0" <= c <= "9":
            val += c
        elif c == '(':
            subResult = calculate_pt1(line, i + 1)
            acc = handleOp(acc, subResult[0], op)
            i = subResult[1]
        elif c == ')':
            break
        else:
            raise "c"

        i += 1
    if val != '':
        acc = handleOp(acc, int(val), op)
    return [acc, i]

def calculate_pt2(line, i):
    acc = 0
    val = ''
    op = '+'
    factors = []
    
    while i < len(line):
        c = line[i]

        if c == ' ':
            if val != '':
                acc = handleOp(acc, int(val), op)
                val = ''
        elif c == '+':
            op = c
            i += 1
        elif c == '*':
            factors.append(acc)
            acc = 0
            i += 1
        elif "0" <= c <= "9":
            val += c
        elif c == '(':
            subResult = calculate_pt2(line, i + 1)
            acc = handleOp(acc, subResult[0], op)
            i = subResult[1]
        elif c == ')':
            break
        else:
            raise "c"

        i += 1
    if val != '':
        acc = handleOp(acc, int(val), op)
    for f in factors:
        acc *= f 
        
    return [acc, i]

print(sum([calculate_pt1(entry, 0)[0] for entry in data]))
print(sum([calculate_pt2(entry, 0)[0] for entry in data]))
