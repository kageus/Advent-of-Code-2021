import numpy as np
splitInput = open("./input/input_13.txt").read().split("\n\n")
foldInput = splitInput[1].split("\n")
plotInput = splitInput[0].split("\n")

folds = []
for line in foldInput:
    plane, cord = line[line.index("=")-1:].split("=")
    folds.append((plane, int(cord)))

plotX = []
plotY = []
for line in plotInput:
    x, y = line.split(",")
    plotX.append(int(x))
    plotY.append(int(y))

w, h = max(plotX)+1, max(plotY)+1
a = np.zeros((h,w), np.int32)

for y, x in list(zip(plotY, plotX)):
    a[y][x] = 1

for fold in folds:
    if fold[0] == 'y':
        a = np.delete(a, fold[1], 0)
        b1, b2 = np.vsplit(a, 2)
        b2 = np.flipud(b2)
        a = np.bitwise_or(b1, b2)
    else:
        a = np.delete(a, fold[1], 1)
        b1, b2 = np.hsplit(a, 2)
        b2 = np.fliplr(b2)
        a = np.bitwise_or(b1, b2)
    print(a)
    print(np.count_nonzero(a))
    print("\n----------------------------------\n")
