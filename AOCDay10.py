# part1
with open('inputday10.txt', 'r') as data:
    cycle = 0
    strength = 0
    x = 1
    for line in data:
        if len(line.split()) == 1:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                strength += cycle * x
        else:
            directive, change = line.split()
            cycle += 1
            if (cycle-20) % 40 == 0 or cycle == 20:

                strength += cycle * x
            cycle += 1

            if (cycle-20) % 40 == 0 or cycle == 20:
                strength += cycle * x
            x += int(change)
    # print(cycle)
    # print(strength)

# part2
with open('inputday10.txt', 'r') as data:
    cycle = -1
    x = 1

    CRT = [[0 for a in range(40)] for a in range(6)]

    def update():
        if (cycle) % 40 in (x+1, x, x-1):
            CRT[cycle//40][(cycle) % 40] = "0"
        else:
            CRT[(cycle)//40][(cycle) % 40] = " "

    for line in data:
        if len(line.split()) == 1:
            cycle += 1
            if cycle == 84:
                print(x, cycle)
            update()
        else:
            directive, change = line.split()
            cycle += 1
            if cycle == 84:
                print(x, cycle)
            update()
            cycle += 1
            if cycle == 84:
                print(x, cycle)
            update()
            x += int(change)
    for line in CRT:
        print(line)
