import numpy as np
import sys, math
lineInput = open("./input/input_9.txt").read().split("\n")
w, h = len(lineInput[0]), len(lineInput)

listInput = []
for line in lineInput:
    for character in line:
        listInput.append(int(character))
a = np.array(listInput).reshape(h, w)

print(a)
basins = []
sizeCount = 0

def basinConsumer(a, x, y, sizeCount):
    if a[y][x] == 9:
        return a, sizeCount
    a[y][x] = 9
    sizeCount += 1
    # left
    if x != 0 and a[y][x-1] != 9:
        a, sizeCount = basinConsumer(a, x-1, y, sizeCount)
    # up
    if y != 0 and a[y-1][x] != 9:
        a, sizeCount = basinConsumer(a, x, y-1, sizeCount)
    # right
    if x < len(a[y])-1 and  a[y][x+1] != 9:
        a, sizeCount = basinConsumer(a, x+1, y, sizeCount)
    # down
    if y < len(a)-1 and  a[y+1][x] != 9:
        a, sizeCount = basinConsumer(a, x, y+1, sizeCount)
    return a, sizeCount

# while(len(np.unique(a)) != 1 ):
for y in range(0, h):
    for x in range(0, w):
        a, sizeCount = basinConsumer(a, x, y, sizeCount)
        if sizeCount != 0:
            basins.append(sizeCount)
            if(np.all(a == a[0][0])):
                basins.sort(reverse=True)
                print(f"{basins[0]} * {basins[1]} * {basins[2]} = {math.prod(basins[0:3])}")
                sys.exit()
            sizeCount  = 0
