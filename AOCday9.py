# part one
with open('inputday9.txt', 'r') as data:
    visited = set()
    visited.add((0, 0))

    head = [0, 0]
    tail = [0, 0]
    for line in data:
        dir, mag = line.split()
        mag = int(mag)

        if dir == "R":
            head[0] += mag
        elif dir == "L":
            head[0] -= mag
        elif dir == "D":
            head[1] -= mag
        elif dir == "U":
            head[1] += mag

        if tail[0] != head[0] and tail[1] != head[1]:
            xdiff = head[0] - tail[0]
            ydiff = head[1] - tail[1]
            if abs(xdiff) == 1 and abs(ydiff) == 1:
                continue

            if abs(xdiff) == 1:
                tail[0] += xdiff
                if ydiff > 0:
                    tail[1] += 1
                elif ydiff < 0:
                    tail[1] -= 1
                visited.add(tuple(tail))
            elif abs(ydiff) == 1:
                tail[1] += ydiff

                if xdiff > 0:
                    tail[0] += 1

                elif xdiff < 0:
                    tail[0] -= 1
                visited.add((tuple(tail)))

        if tail[1] == head[1]:
            while tail[0] + 1 < head[0]:  # Less on the x coord
                tail[0] += 1
                visited.add(tuple(tail))
            while tail[0] - 1 > head[0]:  # greater on the x coord
                tail[0] -= 1
                visited.add((tuple(tail)))
        elif tail[0] == head[0]:
            while tail[1] + 1 < head[1]:  # Less on the y coord
                tail[1] += 1
                visited.add(tuple(tail))
            while tail[1] - 1 > head[1]:  # greater on the y coord
                tail[1] -= 1
                visited.add((tuple(tail)))

    print(len(visited))

# part 2
with open('inputday9.txt', 'r') as data:
    visited = {(0, 0)}
    knots = [[0, 0] for i in range(10)]
    for line in data:
        t, d = line.split()
        d = int(d)
        for _ in range(d):
            if t == 'R':
                knots[0][1] += 1
            elif t == 'U':
                knots[0][0] -= 1
            elif t == 'L':
                knots[0][1] -= 1
            else:
                knots[0][0] += 1
            for i in range(1, 10):
              # move up each knot step by step. By doing so, we can the difference between a given node by 2. It can only be L2, R2, U2, D2 or Diag 2
                # u/D and L/r 2, move diag 1 (most the diff can be)
                if abs(knots[i][0]-knots[i-1][0]) == 2 and abs(knots[i][1]-knots[i-1][1]) == 2:
                    knots[i][0] = (knots[i][0]+knots[i-1][0])//2
                    knots[i][1] = (knots[i][1]+knots[i-1][1])//2
                if abs(knots[i][0]-knots[i-1][0]) == 2:  # left or right 2
                    knots[i][0] = (knots[i][0]+knots[i-1][0])//2
                    knots[i][1] = knots[i-1][1]
                if abs(knots[i][1]-knots[i-1][1]) == 2:  # up or down 2
                    knots[i][1] = (knots[i][1]+knots[i-1][1])//2
                    knots[i][0] = knots[i-1][0]

            visited.add((knots[9][0], knots[9][1]))

    print(len(visited))
