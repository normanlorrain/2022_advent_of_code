test="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


if True :
    lines = test.splitlines()
else:
    lines = open('day12.txt')
lines = iter(lines)

class Position: # top left is 0,0
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def __init__(self,x,y, elevation) -> None:
        self.x = x 
        self.y = y
        self.start = False
        self.end = False
        
        self.ch = elevation 
        self.elevation = ord(elevation) - ord('a')
        self.neighbors = []

        self.n = None
        self.s = None
        self.w = None 
        self.e = None 

        pass
    def tup(self):
        return (self.x,self.y)

# the elevation of the destination square can be at most one higher than the elevation of your current square
def canReach(here,there):
    return there.elevation - here.elevation
    

def checkNeighbors():
    for pos in grid.values():
        row = pos.x
        col = pos.y

        neighbors={}
        if col < width-1:
            e = grid[row,col+1]
            if (step:=canReach(pos,e)) <= 1:
                pos.e = e
                neighbors[e] = step
                # pos.neighbors.append(e)
        if row > 0:
            n = grid[row-1,col]
            if (step:=canReach(pos, n)) <=1:
                pos.n = n
                neighbors[n] = step
                # pos.neighbors.append(n)

        if row < height-1:
            s = grid[row+1,col]
            if (step:=canReach(pos, s)) <=1:
                pos.s = s
                neighbors[s] = step
                # pos.neighbors.append(s)

        if col > 0:
            w = grid[row,col-1]
            if (step:=canReach(pos, w)) <= 1:
                pos.w =w
                neighbors[w] = step
                # pos.neighbors.append(w)
        for neighbor in sorted(neighbors, key=neighbors.get,reverse=True):
            pos.neighbors.append(neighbor)
            pass
        
        





start = None
end = None
grid={}
row = 0

for line in lines:
    col = 0
    for char in line.strip():
        if char == 'S':
            pos =  Position(row,col,'a')
            pos.start = True
            pos.ch = 'S'
            start = pos

        elif char == 'E':
            pos =  Position(row,col,'z')
            pos.end = True
            pos.ch= 'E'
            end = pos
        
        else:
            pos =  Position(row,col,char)
        grid[(row,col)] = pos

        col+= 1
    row +=1

width = col
height = row



checkNeighbors()


def printGrid(trail):
    for row in range(height):
        for col in range(width):
            cell = grid[(row,col)].tup()
            ch = grid[(row,col)].ch
            if cell in trail:
                print(ch.upper(),end='')
            else:
                print(ch,end='')
        print()
    print()


print(f"Start, {start}, End: {end}")
paths = []
best = None
def findPath(pos, trail= []):
    print('pos',pos)
    global best
    if best and len(trail)>= best:  
        return False 
    if pos == end:
        trail.append((pos.x,pos.y))
        best = len(trail)
        paths.append(trail)

        return True
    if len(pos.neighbors) > 1:
        foundPath = False
        for neighbor in list(pos.neighbors):
            if (neighbor.x, neighbor.y) in trail:
                continue # We've been here before, so don't add it again.
            
            if findPath(neighbor, trail + [(pos.x,pos.y)]): # Pass by value here:
                foundPath = True
            else:
                pos.neighbors.remove(neighbor) 
        return foundPath
    else:
        return False


for neighbor in start.neighbors:
    findPath(neighbor, [(start.x, start.y)])

pass
print(len(paths))
print("Part One,  ", best - 1)


