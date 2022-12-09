import math 
test="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""



if False:
    lines = test.splitlines()
else:
    import os
    scriptFile=os.path.basename(__file__)
    dataFile=f"{scriptFile[:-3]}.txt"
    lines = open(dataFile)

# x,y
class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

def sub( head,tail):
    return Vector(head.x-tail.x, head.y-tail.y)
def abs( v):
    return math.sqrt(v.x**2 + v.y**2)
# def dis( head,tail ):
#     return abs(sub(head,tail))

head = Vector(0,0)
tail = Vector(0,0)

visited = set()

visited.add((tail.x,tail.y))

for line in lines:
    direction, steps = line.split()

    for step in range(int(steps)):
        match direction:
            case 'U':
                head.y +=1
            case 'D':
                head.y -=1
            case 'L':
                head.x -= 1
            case 'R':
                head.x += 1


        delta = sub(head,tail)
        distance = abs(delta)
        
        if distance >=2:
            if (delta.x !=0) and (delta.y!=0): # Diagonal
                if (delta.x > 0) and delta.y > 0:
                    tail.x += 1
                    tail.y += 1
                if (delta.x > 0) and delta.y < 0:
                    tail.x += 1
                    tail.y -= 1
                if (delta.x < 0) and delta.y > 0:
                    tail.x -= 1
                    tail.y += 1
                if (delta.x < 0) and delta.y < 0:
                    tail.x -= 1
                    tail.y -= 1
            else:
                if (delta.x > 0): 
                    tail.x += 1
                if (delta.x < 0): 
                    tail.x -= 1
                if delta.y > 0:
                    tail.y += 1
                if delta.y < 0:
                    tail.y -= 1
        visited.add((tail.x,tail.y))
        pass




print("Part One", len(visited))
pass
