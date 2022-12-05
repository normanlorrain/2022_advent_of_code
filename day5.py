import string
import re


test="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


f = test.splitlines()
f = iter(f)
f = open("day5.txt")

stacks = []
while True:
    line = next(f)
    if stacks == []: # Initialize
        for i in range(1,len(line),4):
            stacks.append([])


    if line[1] == '1': # We've reached column labels.
        break
    col = 0

    for i in range(1,len(line),4):
        c = line[i]
        # print(c)
        if c != ' ':

            stacks[col].insert(0,c)
        col +=1

blank = next(f)  # Skip the blank lines
while True:
    try:
        line = next(f)
    except StopIteration:
        break

    m = re.search('\D+(\d+)\D+(\d+)\D+(\d+)', line)
    n,src,dst = map(int,m.group(1,2,3))


    print(f"MOVING {n} FROM {src} to {dst}")

    if False:
        for i in range(0,n):
            c = stacks[src-1].pop()
            stacks[dst-1].append(c)
            pass
    else:
        c = stacks[src-1][-n:]
        stacks[src-1] = stacks[src-1][:-n]
        stacks[dst-1].extend(c)
    
for stack in stacks:
    print(stack.pop(),end='')
pass