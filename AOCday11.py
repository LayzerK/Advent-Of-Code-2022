from collections import deque
import re


class Monke:
    def __init__(self, id=-1, optype="", multiple=-1, monkebiz=0, test=0, truepartner=0, falsepartner=0):
        self.id = id
        self.items = deque()
        self.optype = optype
        self.multiple = multiple
        self.monkebiz = monkebiz
        self.truepartner = truepartner
        self.falsepartner = falsepartner
        self.test = test

    def turn(self):
        while self.items:
            curr = self.items.popleft()
            # print(curr)
            self.monkebiz += 1

            if self.optype == "plus":
                curr += self.multiple

            else:
                if isinstance(self.multiple, int):
                    curr *= self.multiple
                else:
                    curr *= curr

            #curr //= 3
            curr %= 9699690
            # LCM of all the monke
            if curr % self.test == 0:
                yield ((self.truepartner, curr))
            else:
                yield ((self.falsepartner, curr))


with open('inputday11.txt', 'r') as data:
    monkeys = []

    for line in data:

        curr = monkeys[-1] if monkeys else None

        if line.startswith('Monkey'):
            idgiver = line.split()
            monkeys.append(Monke())
            monkeys[-1].id = int(idgiver[1][0])

        if line.startswith('  Starting'):
            starting = re.split(': |, ', line)
            for item in starting:
                if item == "  Starting items":
                    continue
                curr.items.append(int(item))

        if line.startswith("  Operation:"):
            op = line.split()

            operation = op[4]
            mult = op[5]

            if operation == "*":
                curr.optype = "times"
            else:
                curr.optype = "plus"
            curr.multiple = int(mult) if mult != "old" else mult

        if line.startswith("  Test: divisible by"):
            test = line.split()

            curr.test = int(test[3])

        if line.startswith("    If true: throw to monkey"):
            throw = line.split()

            curr.truepartner = int(throw[5])
        if line.startswith("    If false: throw to monkey"):
            throw = line.split()

            curr.falsepartner = int(throw[5])

    for round in range(20):
        for monkey in monkeys:
            for receiver, item in monkey.turn():
                monkeys[receiver].items.append(item)

    top = []
    for monkey in monkeys:
        top.append(monkey.monkebiz)
    # too lazy for heap tbh...

    print(sorted(top, reverse=True)[:2])
