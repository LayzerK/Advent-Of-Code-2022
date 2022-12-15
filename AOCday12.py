from collections import deque
with open('inputday12.txt', 'r') as data:
    rLen = 0
    cLen = 0
    grid = [[]]
    q = deque()
    visited = set()
    mapping = {chr(ord('a') + x): x for x in range(26)}
    for line in data:
        line = line.rstrip()
        for col, val in enumerate(line):
            if val == "S":
                start = (rLen, col, 0)
                grid[rLen].append(0)
            elif val == "E":
                end = (rLen, col)
                grid[rLen].append(25)
            elif val == "a":
                q.append((rLen, col, 0))
                visited.add((rLen, col))
                grid[rLen].append(0)
            else:
                grid[rLen].append(mapping[val])
        Len = len(line)
        rLen += 1
        cLen = len(line)
        grid.append([])
    row = 0

    minimum = 0
    ()
    q.append((start))
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited.add((start[0], start[1]))
    while q:
        row, col, steps = q.popleft()
        print(row, col, steps)
        if (row, col) == end:
            print(steps)
            break
        for dr, dc in directions:

            NR = row + dr
            NC = col + dc
            print(NR, row, NC, col)
            if NC in range(cLen) and NR in range(rLen) and grid[NR][NC] <= grid[row][col] + 1 and (NR, NC) not in visited:
                q.append((NR, NC, steps+1))
                visited.add((NR, NC))
