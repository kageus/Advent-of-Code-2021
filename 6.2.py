# refactored for scale
from collections import defaultdict
dataInput = open("./input/input_6.txt").read().split(",")

fishGroup   = [int(x) for x in dataInput]
fishDict    = defaultdict(int)
for i in fishGroup:
    fishDict[i] += 1
updatedFish = defaultdict(int)

days    = 256
day     = 1

while day <= days:
    for key, value in fishDict.items():
        if key == 0:
            updatedFish[6] = value + updatedFish[6]
            updatedFish[8] = value
        else:
            updatedFish[key -1] = value + updatedFish[key - 1]
    fishDict = updatedFish.copy()
    updatedFish.clear()
    day += 1

sum = 0
print(fishDict)
for value in fishDict.values():
    sum += value
print(sum) # 1749945484935