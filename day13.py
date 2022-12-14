test="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""



if False:
    lines = test.splitlines()
else:
    lines = open('day13.txt')
lines = iter(lines)

def mysort( left, right):
    print(left, right)
    if type(left) == int and type(right) ==int:
        if left < right:
            return -1
        elif left > right:
            return +1
        else:
            return 0 # "Otherwise, the inputs are the same integer; continue checking the next part of the input."
    elif type(left) == list and type(right) == list:

        for i in range( min( len(left),len(right))):
            ret = mysort(left[i],right[i])
            if ret==0:
                continue
            else:
                return ret
        if len(left) < len(right):
            return -1
        elif len(right) < len(left):
            return +1
        else:  
            return 0

    elif type(left) == int and type(right) == list:
        return mysort([left],right)
        
    elif type(left) == list and type(right) ==int:
        return mysort(left,[right])
    else:
        raise Exception
    pass

packets = []
for line in lines:
    if len(line)> 1:
        expression = line.strip()
        exec(f'val = {expression}')
        packets.append(val)

from functools import cmp_to_key
divOne = [[2]]
divTwo = [[6]]
packets.append(divOne)
packets.append(divTwo)
sPackets = sorted(packets, key=cmp_to_key(mysort))




one = sPackets.index(divOne) + 1
two = sPackets.index(divTwo) + 1
pass

print("Part Two", one*two)




