data="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

def operand(token):
    if token == 'old':
        return None
    else:
        return int(token)




class Monkey:
    magic = 1

    def __init__(self, number, items, operation, test,trueThrow, falseThrow) -> None:
        self.number = int(number)
        self.items = items
        self.inspections = 0

        # Operation are the form of {lhs} {operator} {rhs}.  We'll assume 0 means use the old number
        self.lhs = operand( operation[0])
        self.rhs = operand(operation[2])
        match operation[1]:
            case '+':
                self.operator = True
            case '*':
                self.operator = False
            case _:
                raise Exception("bad operator")


        # Test
        self.testDivisible = int(test)
        Monkey.magic *= self.testDivisible

        self.trueThrow = trueThrow
        self.falseThrow = falseThrow

    # def catch(self, item):
        

if False:
    lines = data.splitlines()
else:
    lines = open('day11.txt')
lines = iter(lines)

monkeys = []

for line in lines:
    tokens = line.split()
    if tokens[0] == 'Monkey':
        number = int(tokens[1][:-1]) # Chop off ending ':'

        # Starting Items 
        line = next(lines).split(':')
        items = line[1].strip()
        items = items.replace(',','')
        items = items.split(' ')
        items = list(map(int,items))

        # Operation
        tokens = next(lines).split()
        operation = tokens[3:]

        # Test
        tokens = next(lines).split()
        test = tokens[-1]

        # true
        tokens = next(lines).split()
        trueThrow =  int(tokens[-1])

        # false 
        tokens = next(lines).split()
        falseThrow =  int(tokens[-1])
        
        # Have everything, make a monkey!
        monkeys.append( Monkey(number, items, operation, test, trueThrow, falseThrow ) )

    try:
        blank = next(lines).split()
        length = len(blank)
        if length:
            pass
            # print ("ERROR")
    except:
        break  # End of file 


n=0
for round in range(10000):
    n +=1
    print ('Round ', n)
    for monkey in monkeys:
        # print  (f'Monkey {monkey.number}')
        for item in list(monkey.items):
            monkey.inspections +=1
            # print (f'  Monkey inspects an item with a worry level of {item}')
            lhs = monkey.lhs if monkey.lhs else item
            rhs = monkey.rhs if monkey.rhs else item
            if monkey.operator:
                    worry = lhs + rhs
                    # print (f'    {worry} = {lhs} + {rhs}')
            else:
                    worry = lhs * rhs
                    # print (f'    {worry} = {lhs} * {rhs}')
                # # print ("ERROR case")
            # worry = worry // 3 
            # # print ("    Monkey gets bored with item. Worry level is divided by 3 to ", worry)
            # print (f'   worry {worry}')
            test = (worry % monkey.testDivisible) == 0
            if test:
                monkeys[monkey.trueThrow].items.append(worry % Monkey.magic)
                # print ("    Current worry level is divisible by", monkey.testDivisible)
                # print (f"    Item with worry level {worry} is thrown to monkey {monkey.trueThrow}")
            else:
                monkeys[monkey.falseThrow].items.append(worry % Monkey.magic)
                # print ("    Current worry level is not divisible by", monkey.testDivisible)
                # print (f"    Item with worry level {worry} is thrown to monkey {monkey.falseThrow}")
            monkey.items.remove(item)

inspections = []
for monkey in monkeys:
    # print (f'Monkey {monkey.number}:',end='')
    for item in monkey.items:
        pass
        # print (f'{item} ',end='')
    # print ()
    print ( f'Monkey {monkey.number} inspected items {monkey.inspections} times.')
    inspections.append(monkey.inspections)

inspections = sorted(inspections)
print ("Part One and Two", inspections[-1]* inspections[-2] )
