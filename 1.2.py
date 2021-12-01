dataInput = open("./input/input_1.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

countIncrease = 0
listOfWindows = []
for x in range(0, len(lineList)-2):
    tupleWindow = ( int(lineList[x]), int(lineList[x+1]), int(lineList[x+2]) )
    listOfWindows.append(tupleWindow)

window_sums = [sum(window) for window in listOfWindows]

for x in range(1, len(window_sums)):
    if(window_sums[x] > window_sums[x-1]):
        countIncrease += 1

f"Increased Depths:  {countIncrease}"