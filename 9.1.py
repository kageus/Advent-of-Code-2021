import numpy as np
lineInput = open("./input/input_9.txt").read().split("\n")
w, h = len(lineInput[0]), len(lineInput)

listInput = []
for line in lineInput:
    for character in line:
        listInput.append(int(character))
a = np.array(listInput).reshape(h, w)

riskLevel = 0
for y in range(0, h):
    for x in range(0, w):
        lowestCount = 0
        # left
        if x == 0:
            lowestCount += 1
        elif a[y][x] < a[y][x-1:x]:
            lowestCount += 1
        # right
        if x == w -1:
            lowestCount += 1
        elif a[y][x] < a[y][x+1:x+2]:
            lowestCount += 1
        # up
        if y == 0:
            lowestCount += 1
        elif a[y][x] < a[y-1][x]:
            lowestCount += 1
        # down
        if y == h -1:
            lowestCount += 1
        elif a[y][x] < a[y+1][x]:
            lowestCount += 1
        # check if lowest
        if lowestCount == 4:
            riskLevel += int(a[y][x])+1

print(riskLevel)