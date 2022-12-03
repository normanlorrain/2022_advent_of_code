test="""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

f = test.splitlines()
f = open("day1.txt")
elves=[0]
elf = 0
for i in f:
    n = int(i.strip() or 0)
    if n:
        elves[elf]+=n
    else:
        elf+=1
        elves.append(0)
most = max(elves)
print(most)
max_index = elves.index(most)

top_three = sorted(elves,reverse=True)[0:3] 
print(top_three)
print(sum(top_three))