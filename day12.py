test="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


if True:
    lines = test.splitlines()
else:
    lines = open('day12.txt')
lines = iter(lines)

class Position: # top left is 0,0
    def __init__(self,x,y, elevation) -> None:
        self.x = x 
        self.y = y
        self.start = False
        self.end = False
        
        self.elevation = ord(elevation) - ord('a')
        self.neighbors = []

        self.n = None
        self.s = None
        self.w = None 
        self.e = None 

        pass

# the elevation of the destination square can be at most one higher than the elevation of your current square
def canReach(here,there):
    if there.elevation - here.elevation <=1:
        return True

def checkNeighbors():
    for pos in grid.values():
        row = pos.x
        col = pos.y
        if row > 0:
            n = grid[row-1,col]
            if canReach(pos, n):
                pos.n = n
                pos.neighbors.append(n)

        if row < height-1:
            s = grid[row+1,col]
            if canReach(pos, s):
                pos.s = s
                pos.neighbors.append(s)

        if col > 0:
            w = grid[row,col-1]
            if canReach(pos, w):
                pos.w =w
                pos.neighbors.append(w)

        if col < width-1:
            e = grid[row,col+1]
            if canReach(pos,e):
                pos.e = e
                pos.neighbors.append(e)




start = None
end = None
grid={}
row = 0

for line in lines:
    col = 0
    for char in line:
        if char == 'S':
            pos =  Position(row,col,'a')
            pos.start = True
            start = pos

        elif char == 'E':
            pos =  Position(row,col,'z')
            pos.end = True
            end = pos
        
        else:
            pos =  Position(row,col,char)
        grid[(row,col)] = pos

        col+= 1
    row +=1

width = col
height = row



checkNeighbors()


# print(grid)


paths = []
def findPath(pos, trail= []):
    for neighbor in pos.neighbors:
        trail.append((pos.x,pos.y))
        paths.append(findPath(neighbor, trail))   #Ugh.  It's going back and forth.  Need to prevent backtracking.  TODO.


findPath(start)

print(paths)

