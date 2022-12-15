from functools import cmp_to_key


def compare(a, b):
    for x, y in zip(a, b):
        if type(x) == int and type(y) == int:
            c = x - y
        elif type(x) == list and type(y) == list:
            c = compare(x, y)
        elif type(x) == int and type(y) == list:
            c = compare([x], y)
        elif type(x) == list and type(y) == int:
            c = compare(x, [y])
        if c != 0:
            return c
    return len(a) - len(b)  # for tie breaking


# p1
with open('inputday13.txt', 'r') as data:
    left = None
    right = None
    cnt = 0
    ans = 0
    for line in data:
        if line.startswith("["):
            if left is None:
                left = eval(line)
            else:
                right = eval(line)
        else:
            left = None
            right = None
        if left is not None and right is not None:
            ordering = compare(left, right) < 0
            cnt += 1
            if ordering:
                ans += cnt

# p2
with open('inputday13.txt', 'r') as data:

    arr = []
    x = [[2]]
    y = [[6]]
    for line in data:
        if line.startswith("["):
            arr.append(eval(line))
    arr.append(x)
    arr.append(y)
    arr.sort(key=cmp_to_key(compare))
    # print(arr)
    print((arr.index(x) + 1) * (arr.index(y) + 1))
