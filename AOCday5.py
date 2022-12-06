with open('inputday5.txt', 'r') as data:
    stacks = [[] for x in range(9)]
    mapping = {1: 0, 5: 1, 9: 2, 13: 3, 17: 4, 21: 5, 25: 6, 29: 7, 33: 8}
    for line in data:
        if line.startswith(" 1 "):
            break
        for i, n in enumerate(line):
            if i in mapping and n.isalpha():
                stacks[mapping[i]].append(n)
        # creates initial stacks

    for container in range(9):
        stacks[container].reverse()
    for line in data:
        if line.startswith('move'):

            arr = line.split()

            tomove = int(arr[1])
            ogloc = int(arr[3]) - 1
            newloc = int(arr[5]) - 1

            moved = []

            for container in range(tomove):
                moved.append(stacks[ogloc].pop())

            for container in (moved):
                stacks[newloc].append(container)
    for container in range(9):
        if len(stacks[container]) > 0:
            print(stacks[container][-1], end="")
