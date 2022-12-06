input = open("input.txt", "r")

curr = 0
best = 0
total = []

for cal in input.readlines():
    cal = cal.strip()

    if len(cal) > 0:
        curr += int(cal)
    else:
        best = max(curr, best)
        total.append(curr)
        curr = 0
print(sum(sorted(total, reverse=True)[:3]))
print(best)
