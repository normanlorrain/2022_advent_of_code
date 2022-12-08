test="""30373
25512
65332
33549
35390"""


N=1
S=2
E=3
W=4



if False:
    lines = test.splitlines()
else:
    import os
    scriptFile=os.path.basename(__file__)
    dataFile=f"{scriptFile[:-3]}.txt"
    lines = open(dataFile)

class Tree:
    def __init__(self, height, row, col) -> None:
        print(f"{row},{col} = {height}")
        self.height = height
        self.row = row
        self.col = col
        self.n = None
        self.s = None
        self.e = None
        self.w = None
    def findPath(self,direction,height):
        if direction == N:
            if self.n == None:
                return True
            elif self.n.height >= height:
                return False
            else: 
                return self.n.findPath(direction,height)
        elif     direction ==  S:
            if self.s == None:
                return True
            elif self.s.height >= height:
                return False
            else: 
                return self.s.findPath(direction,height)
        elif     direction ==   E:
            if self.e == None:
                return True
            elif self.e.height >= height:
                return False
            else:
                return self.e.findPath(direction,height)
        elif     direction ==   W:
            if self.w == None:
                return True
            elif self.w.height >= height:
                return False
            else: 
                return self.w.findPath(direction,height)
        

    def scenicScore(self,direction,height):
        if direction == N:
            if self.n == None:
                return 0
            elif self.n.height >= height:
                return 1
            else: 
                return 1 + self.n.scenicScore(direction,height)
        elif     direction ==  S:
            if self.s == None:
                return 0
            elif self.s.height >= height:
                return 1
            else: 
                return 1 + self.s.scenicScore(direction,height)
        elif     direction ==   E:
            if self.e == None:
                return 0
            elif self.e.height >= height:
                return 1
            else:
                return 1 + self.e.scenicScore(direction,height)
        elif     direction ==   W:
            if self.w == None:
                return 0
            elif self.w.height >= height:
                return 1
            else: 
                return 1 + self.w.scenicScore(direction,height)
    













# Build the grid
trees = []
row = 0
for line in lines:
    line = line.strip()
    trees.append([])
    col = 0
    for height in line:
        trees[row].append(Tree(int(height), row, col))
        col += 1
    row +=1

# Connect the nodes

gridWidth = len(trees)
gridHeight = len(trees[0])

row = 0
col = 0

for treeRow in trees:
    col = 0
    for tree in treeRow:
        if row > 0:
            tree.n = trees[row-1][col]
        if row < gridHeight - 1:
            tree.s = trees[row+1][col]
        if col < gridWidth -1:
            tree.e = trees[row][col+1]
        if col > 0:
            tree.w = trees[row][col-1]
        col +=1
    row += 1




# Find the number visible
visible = 0
row = 0
col = 0
for treeRow in trees:
    col = 0
    for tree in treeRow:
        print(f"Row,col {row+1},{col+1}", end='')
        foundPath = tree.findPath(N, tree.height) or tree.findPath(S, tree.height) or tree.findPath(E, tree.height) or tree.findPath(W, tree.height)

        if foundPath:
            visible += 1
            print(" YES")
        else:
            print('')
        col +=1
    row += 1

pass
print("Part one", visible)


# Part Two
# Find the scenic score
scores = []
row = 0
col = 0
for treeRow in trees:
    col = 0
    for tree in treeRow:
        score = tree.scenicScore(N, tree.height) * tree.scenicScore(S, tree.height) * tree.scenicScore(E, tree.height) * tree.scenicScore(W, tree.height)

        # print(f"Row,col {row+1},{col+1} {score}")
        print(f"{score} ",end='')
        scores.append(score)
        col +=1
    print()
    row += 1

print(f"Part Two: {max(scores)}")