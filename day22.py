import collections
from itertools import islice

with open("input/day22", "r") as input:
    data = input.read().split("\n\n")
    data = [[int(entry) for entry in data[i].split("\n")[1:] if entry != ''] for i in range(len(data))]

def buildDecks():
    return [collections.deque(entry) for entry in data]

def gameFinished(decks):
    for d in decks:
        if len(d) == 0:
            return True
    return False

def step(d0, d1):
    c0 = d0.popleft()
    c1 = d1.popleft()
    if c0 > c1:
        d0.append(c0)
        d0.append(c1)
    elif c0 < c1:
        d1.append(c1)
        d1.append(c0)

def calcScores(decks):
    scores = []
    for d in decks:
        scores.append(sum([d[i] * (len(d) - i) for i in range(len(d))]))
    return tuple(scores)

def part1():
    decks = buildDecks()
    while not gameFinished(decks):
        step(decks[0], decks[1])

    print("Part 1: " + str(sum(calcScores(decks))))

def step_pt2(d0, d1):
    c0 = d0.popleft()
    c1 = d1.popleft()
    winner = None
    if len(d0) < c0 or len(d1) < c1:
        winner = 0 if c0 > c1 else 1
    else:
        winner = game_pt2([collections.deque(islice(d0, 0, c0)), collections.deque(islice(d1, 0, c1))])[0]

    if winner == 0:
        d0.append(c0)
        d0.append(c1)
    else:
        d1.append(c1)
        d1.append(c0)

def game_pt2(decks):
    scores = set()
    while not gameFinished(decks):
        score = calcScores(decks)
        if score in scores:
            return (0, score)
        scores.add(score)
        step_pt2(decks[0], decks[1])

    return (0, calcScores(decks)) if len(decks[1]) == 0 else (1, calcScores(decks))

def part2():
    winner = game_pt2(buildDecks())
    print("Part 2: " + str(winner[1][winner[0]]))

part1()
part2()
