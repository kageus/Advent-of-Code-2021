# quick dirty and totally unscalable
dataInput = open("./input/input_6.txt").read().split(",")

fishGroup   = [int(x) for x in dataInput]
newFish     = []
days        = 80
day = 1
while day <= days:
    for i in range(0, len(fishGroup)):
        fishGroup[i] -= 1
        if fishGroup[i] == -1:
            fishGroup[i] = 6
            newFish.append(8)
    fishGroup += newFish
    newFish = []
    day += 1
print(len(fishGroup))