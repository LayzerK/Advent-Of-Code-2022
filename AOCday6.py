with open('inputday6.txt', 'r') as data:
    for line in data:
        for i in range(13, len(line)):
            if len(set(line[i-13:i+1])) == 14:
                print(i+1)
                break
