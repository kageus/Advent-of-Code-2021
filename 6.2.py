from collections import Counter
dataInput = open("./input/input_6.txt").read().split(",")

fishGroup   = [int(x) for x in dataInput]
fishCount   = Counter(fishGroup)
fishDict    = dict(fishCount)

updatedFish = {}

days        = 256
day = 1

while day <= days:
    for key, value in fishDict.items():
        if key == 0:
            if(updatedFish.get(6)):
                updatedFish[6] = value + updatedFish[6]
            else:
                updatedFish[6]      = value
            updatedFish[8]      = value
        else:
            if(updatedFish.get(key -1)):
                updatedFish[key -1] = value + updatedFish[key - 1]
            else:
                updatedFish[key - 1] = value
    fishDict = updatedFish
    updatedFish = {}
    day += 1

sum = 0
print(fishDict)
for value in fishDict.values():
    sum += value
print(sum)