import math 
test="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""



if False:
    lines = test.splitlines()
else:
    lines = open('day9.txt')

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
tail = []
for i in range(9):
    tail.append(Vector(0,0))


visited = set()

visited.add((tail[8].x,tail[8].y))

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

        for i in range(9):
            if i==0 :
                delta = sub(head,tail[0])
            else:
                delta = sub(tail[i-1],tail[i])
            distance = abs(delta)
            
            if distance >=2:
                if (delta.x !=0) and (delta.y!=0): # Diagonal
                    if (delta.x > 0) and delta.y > 0:
                        tail[i].x += 1
                        tail[i].y += 1
                    if (delta.x > 0) and delta.y < 0:
                        tail[i].x += 1
                        tail[i].y -= 1
                    if (delta.x < 0) and delta.y > 0:
                        tail[i].x -= 1
                        tail[i].y += 1
                    if (delta.x < 0) and delta.y < 0:
                        tail[i].x -= 1
                        tail[i].y -= 1
                else:
                    if (delta.x > 0): 
                        tail[i].x += 1
                    if (delta.x < 0): 
                        tail[i].x -= 1
                    if delta.y > 0:
                        tail[i].y += 1
                    if delta.y < 0:
                        tail[i].y -= 1
            visited.add((tail[8].x,tail[8].y))
        pass




print("Part Two", len(visited))
pass
