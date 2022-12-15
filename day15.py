import re 
test="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""



offset = -2
width = 25 + 1 + 2
height = 22 + 1


cave = [['.' for x in range(width)] for y in range(height)]
    
def printCave():
    print('~'*width)
    for y in range(height):
        for x in range(width):
            print(cave[y][x],end='')
        print()





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



    # line=line.strip()  # '498,4 -> 498,6 -> 496,6'
    # pointsString = re.findall(r'(\d+),(\d+)',line)  #[('498', '4'), ('498', '6'), ('496', '6')]
    # points = [(int(x[0]),int(x[1])) for x in pointsString]

    # points = iter(points)
    # start = next(points)
    # for end in points:
    #     fillIn(start,end)
    #     printCave()
    #     start = end



if __name__ == "__main__":
    if True:
        lines = test.splitlines()
    else:
        lines = open('day15.txt')
    lines = iter(lines)

    printCave()
    for line in lines:
        points = re.findall(r'x=(-?\d+), y=(-?\d+)',line)  #"Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
        sensor = (int(points[0][0]), int(points[0][1]))
        beacon = (int(points[1][0]), int(points[1][1]))
        cave[sensor[1]][sensor[0] - offset] = 'S'
        cave[beacon[1]][beacon[0] - offset] = 'B'

        # "Manhattan Distance"
        d = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        pass
    printCave()
