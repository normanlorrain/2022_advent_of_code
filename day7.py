import re 

example="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

class File:
    name = None
    parent = None
    size = 0
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        parent.grow(size)



class Dir:
    name = None
    subDirs = []
    files = []
    parent = None
    size = 0

    def __init__(self, name, parent) -> None:
        # print("")
        self.name = name
        self.subDirs = []
        self.files = []
        self.parent = parent
        self.size = 0

    def grow(self, size):
        self.size += int(size)
        if self.parent:
            self.parent.grow(size)


    def cd(self, name):
        if name == '/':
            return root
        if name == '..':
            return self.parent
        for i in self.subDirs:
            if i.name == name:
                return i
        raise Exception("cd: Not found")



root = None

# "Modes" of line output
CMD = 1
LS = 2

def day( lines ):
    lines = iter(lines)
    current = root
    lineMode = CMD
    line = next(lines)
    while True:
        print(line.strip())
        # re.search("(\W+)\s(\W+)\s(\w+)")
        if  lineMode == CMD:   # In this mode, only cd and ls 
            tokens = line.split()
            if tokens[1] == 'ls':
                lineMode = LS
                line = next(lines)
                continue

            if tokens[1] == 'cd':
                name = tokens[2]
                current = current.cd(name)
                line = next(lines)
                continue
        if  lineMode == LS:   # In this mode, only dirs or files.
            tokens = line.split()
            if tokens[0] == '$':
                lineMode = CMD # Switch mode and go back to reading rest of cmd;
                                # don't read next line here.
                continue
            if tokens[0] == 'dir':
                current.subDirs.append(Dir(tokens[1], current))
                line = next(lines)
                continue
            # At this point must be a size and file name
            size,name = tokens
            current.files.append(File(name,size, current))
            line = next(lines)





        # match 


def walk(directory: Dir, level = 0):
    smallDirTotal = 0
    prefix = ' '*level*4
    print(f"{prefix}{directory.name} : {directory.size}")
    for f in directory.files:
        print(f"{prefix}    {f.name}, {f.size}")

    for d in directory.subDirs:
        if d.size <=100000:
            smallDirTotal += d.size
        smallDirTotal += walk(d, level+1)
    return smallDirTotal

        









import os
scriptFile=os.path.basename(__file__)
dataFile=f"{scriptFile[:-3]}.txt"


# lines = example.splitlines()
lines = open(dataFile)
root = Dir('/',None)
try:
    day(lines)
except StopIteration:
    pass


smallDirTotal = walk(root)
print("Part One", smallDirTotal)
##############################################





### PART TWO  #### 
total = 70000000
update = 30000000
# required = total - update
used = root.size


toRemove = -(total - (update + root.size))

candidates = []
def walkSmallest(directory: Dir, level = 0):
    if directory.size > toRemove:
        candidates.append(directory.size)
    # prefix = ' '*level*4
    # print(f"{prefix}{directory.name} : {directory.size}")
    # for f in directory.files:
    #     print(f"{prefix}    {f.name}, {f.size}")

    for d in directory.subDirs:
        walkSmallest(d, level+1)


walkSmallest(root)  #  17348139 is too high
print("Part Two", min(candidates))
pass