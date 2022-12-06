with open('inputday3.txt', 'r') as data:
    cleaninput = [line.rstrip() for line in data]
    priorities = {}
    total = 0
    for i in range(26):
        priorities[(chr(ord('a')+i))] = i + 1
        priorities[(chr(ord('A')+i))] = i + 27

    for i in range(0, len(cleaninput), 3):
        common = list(set(cleaninput[i]) & set(
            cleaninput[i+1]) & set(cleaninput[i+2]))[0]
        print(common)
        total += priorities[common]

    print(total)
