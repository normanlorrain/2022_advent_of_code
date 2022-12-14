import re 
test="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


width = 15
height = 10

offset = 490
cave=[['']* width]*height
for y in range(height):
    for x in range(width):
        cave[y][x]='.'
    
def printCave():
    print('*'*width)
    for y in range(height):
        for x in range(width):
            print(cave[y][x],end='')
        print()


printCave()

if True:
    lines = test.splitlines()
else:
    lines = open('day14.txt')
lines = iter(lines)


def fillIn( start, end):
    (x1,y1) = start
    (x2,y2) = end

    if x1 == x2:
        if y1<y2:
            ys = list(range(y1,y2+1))
        else:
            ys = list(range(y2,y1+1))
        for y in ys:
            cave[y][x1-offset] = '#'
    if y1 ==y2:
        if x1<x2:
            xs = range(x1,x2+1)
        else:
            xs = range(x2,x1+1)
        for x in xs:
            cave[y1][x-offset] = '#'
    pass


for line in lines:
    line=line.strip()  # '498,4 -> 498,6 -> 496,6'
    pointsString = re.findall(r'(\d+),(\d+)',line)  #[('498', '4'), ('498', '6'), ('496', '6')]
    points = [(int(x[0]),int(x[1])) for x in pointsString]

    points = iter(points)
    start = next(points)
    for end in points:
        fillIn(start,end)
        printCave()
        start = end



