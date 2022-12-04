import re

test="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


f = test.splitlines()
f = open("day4.txt")
countSubsets = 0              # part 1
countIntersections = 0        # part 2
for i in f:
    # first,second = i.split(',-')
    vals = re.split(',|-', i)
    firstBegin,firstEnd, secondBegin, secondEnd = map(int,vals)
    first = set(range(firstBegin,firstEnd+1))
    second = set(range(secondBegin,secondEnd+1))
    if first.issubset(second) or second.issubset(first):
        countSubsets +=1
    if first & second:
        countIntersections +=1

print(countSubsets)
print(countIntersections)


