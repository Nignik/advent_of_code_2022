import sys
import math

class Monkey():

    def __init__(self, items, operation, test, on_true, on_false):
        self.on_false = on_false
        self.on_true = on_true
        self.test = int(test.split(' ')[2])
        self.operation = operation.split(' ')
        self.inspected_items = 0
        self.items = items
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])

    def check_operation(self, i, wtf):
        match self.operation[1]:
            case '*':
                if self.operation[0] == 'old':
                    if self.operation[2] == 'old':
                        self.items[i] = (self.items[i] * self.items[i]) % wtf
                    else:
                        self.items[i] = (self.items[i] * int(self.operation[2])) % wtf
                else:
                    if self.operation[2] == 'old':
                        self.items[i] = (self.items[i] * int(self.operation[0])) % wtf
                    else:
                        self.items[i] = (self.operation[2] * int(self.operation[0])) % wtf
            case '+':
                if self.operation[0] == 'old':
                    if self.operation[2] == 'old':
                        self.items[i] = (self.items[i] * 2) % wtf
                    else:
                        self.items[i] = (self.items[i] + int(self.operation[2])) % wtf
                else:
                    if self.operation[2] == 'old':
                        self.items[i] = (self.items[i] + int(operation[0])) % wtf
                    else:
                        self.items[i] = (int(self.operation[2]) + int(self.operation[0])) % wtf

    def monke_round(self, wtf):
        result = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: []
        }
        for i in range(len(self.items)):
            self.inspected_items += 1
            self.check_operation(i, wtf)
            self.items[i] = int(self.items[i]) // 1
            if int(self.items[i]) % self.test == 0:
                result[int(self.on_true)].append(self.items[i])
            else:
                result[int(self.on_false)].append(self.items[i])

        return result



    def print_attributes(self):
        print(self.items)
        print(self.operation)
        print(self.test)
        print(f'self.on_true: {self.on_true}')
        print(f'self.on_false: {self.on_false}')
        print(self.inspected_items)


def print_monkes(monkeys):
    for monkey in monkeys:
        print(f'monke number {monkey}')
        monkeys[monkey].print_attributes()
        print()


infile = sys.argv[1] if len(sys.argv)>1 else 'input.in'
data = open(infile).read().split('\n')
monkeys = {}
z = 0


for i in range(1, len(data), 7):
    starting_items = data[i].split(':')
    starting_items = starting_items[1].split(',')
    for j in range(len(starting_items)):
        starting_items[j] = starting_items[j].strip()
    operation = data[i + 1].split(':')
    operation = operation[1].split('=')
    operation = operation[1]
    test = data[i + 2].split(':')
    on_true = ''.join(filter(str.isdigit, data[i + 3]))
    on_false = ''.join(filter(str.isdigit, data[i + 4]))
    new_monkey = Monkey(starting_items, operation.strip(), test[1].strip(), on_true, on_false)
    monkeys[z] = new_monkey
    z += 1

print_monkes(monkeys)

wtf = 9699690
#
# for monkey in monkeys.values():
#     wtf *= monkey.test
# print(f'wtf: {wtf}')

for j in range(1, 10001):
    for i in range(len(monkeys)):
        results = monkeys[i].monke_round(wtf)
        for result in results:
            monkeys[result].items.extend(results[result])
        monkeys[i].items.clear()

maxcnt1 = 0
maxcnt2 = 0
inspections = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
    }
print('-------------------------------END--------------------------------')
for i in range(len(monkeys)):
    maxcnt2 = max(maxcnt2, monkeys[i].inspected_items)
    temp = maxcnt2
    if maxcnt1 < maxcnt2:
        maxcnt2 = maxcnt1
        maxcnt1 = temp

    inspections[i] = monkeys[i].inspected_items
    monkeys[i].print_attributes()
    print()

print(inspections)
print(maxcnt1 * maxcnt2)