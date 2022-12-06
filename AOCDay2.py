import sys
import math
import itertools
import functools
import collections
#data = list(map(int, data))
#line = list(map(int, data[0].split(',')))
#dataset = [i.split('\n') for i in sys.stdin.read().strip().split('\n\n')]
#dataset = [[*map(int, i.split('\n'))] for i in sys.stdin.read().strip().split('\n\n')]
with open('day2input.txt', 'r') as data:
    total = 0
    scores = {"X": 1, "Y": 2, "Z": 3}
    same = {"A": "X", "B": "Y", "C": "Z"}
    p2loses = {"B": "X", "C": "Y", "A": "Z"}
    p2wins = {"C": "X", "A": "Y", "B": "Z"}

    for match in data:
        p1, p2 = match.split()

        if p2 == "X":
            you = p2loses[p1]
            total += scores[you]
        elif p2 == "Y":
            you = same[p1]
            total += scores[you]
            total += 3
        else:
            you = p2wins[p1]
            total += 6
            total += scores[you]


print(total)
