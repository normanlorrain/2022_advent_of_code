test="""mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

lines = test.splitlines()
lines = open("day6.txt")

numDistinct = 14   # 4, part 1.  14 part 2
for line in lines:
    for i in range(len(line)):
        marker = line[i:i+numDistinct]
        markerSet = set(marker)
        # print(marker, len(markerSet))
        if len(set(marker)) == numDistinct:
            print(i+numDistinct)
            break   