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
    if type(left) == int and type(right) ==int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None # "Otherwise, the inputs are the same integer; continue checking the next part of the input."
    elif type(left) == list and type(right) == list:

        for i in range( min( len(left),len(right))):
            ret = mysort(left[i],right[i])
            if ret==None:
                continue
            else:
                return ret
        if len(left) < len(right):
            return True
        elif len(right) < len(left):
            return False
        else:  
            return None

    elif type(left) == int and type(right) == list:
        return mysort([left],right)
        
    elif type(left) == list and type(right) ==int:
        return mysort(left,[right])
    else:
        raise Exception
    pass

sum = 0
pairIndex = 0
for line in lines:
    pairIndex += 1
    first = line.strip()
    second = next(lines).strip()
    try:
        blank = next(lines)
    except:
        pass
    exec(f'left = {first}')
    exec(f'right = {second}')

    ret = mysort( left, right )
    if ret:
        sum += pairIndex

print("Part One", sum)




