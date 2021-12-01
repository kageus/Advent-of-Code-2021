dataInput = open("./input/input_1.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

previousDepth = lineList[0]
countIncrease = 0

for depth in lineList:
    if int(depth) > int(previousDepth):
        countIncrease += 1
    previousDepth = depth

f"Increased Depths:  {countIncrease}"
