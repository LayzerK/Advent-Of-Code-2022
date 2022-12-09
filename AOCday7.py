from collections import *
with open('inputday7.txt', 'r') as data:
    lines = data.readlines()

    arr = []

    ans = []

    def search(arr, directory, ans):

        amount = 0

        while len(arr) > 0:
            line = arr.pop().split(' ')

            if line[0] == "$" and line[1] == "cd":
                if line[2] == "..":
                    break
                amount += search(arr, line[2], ans)
            elif line[0] == '$':
                continue
            elif line[0] == 'dir':
                continue
            else:
                amount += int(line[0])

        ans.append(amount)

        return amount

    for line in lines:
        arr.append(line.strip())

    arr.reverse()
    arr.pop()

    search(arr, "/", ans)

    used = 70000000 - max(ans)

    arr = []
    total = 0
    for i in ans:
        if i <= 100000:
            total += i
    print(total)
    for i in range(len(ans)):
        if used + ans[i] >= 30000000:
            arr.append(ans[i])

    print(min(arr))
