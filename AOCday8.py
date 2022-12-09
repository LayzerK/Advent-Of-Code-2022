from collections import *
with open('inputday8.txt', 'r') as data:
    table = []
    for line in data:
        row = [int(x) for x in str(line.rstrip())]

        table.append(row)
    visible = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    best = 0
    for row in range(len(table)):
        for col in range(len(table[0])):
            if row == 0 or row == len(table)-1 or col == 0 or col == len(table[0]) - 1:
                continue
            distance = 1

            for dr, dc in directions:
                NR = row + dr
                NC = col + dc
                dir = 0
                while NR in range(len(table)) and NC in range(len(table[0])):

                    if table[NR][NC] < table[row][col]:
                        dir += 1
                    else:
                        dir += 1
                        break
                    NR += dr
                    NC += dc
                distance *= dir

            best = max(best, distance)

    print(best)
