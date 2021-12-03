dataInput = open("./input/input_3.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

gammaRate   = ''
epsilonRate = ''

bitCount = len(lineList[0])
lineCount = len(lineList)

# find the gamma one bit at a time
for x in range(0, bitCount):
    onesCount = 0
    for line in lineList:
        bit = line[x]
        if bit == '1':
            onesCount += 1
    zeroesCount = lineCount - onesCount
    if onesCount > zeroesCount:
        gammaRate = gammaRate + '1'
    else:
        gammaRate = gammaRate + '0'

# epsilon is inverted gamma 
for i in range(bitCount):
    if gammaRate[i] == '1':
        epsilonRate += '0'
    else:
        epsilonRate += '1'

# convert to integers
gammaInt   = int(f"0b{gammaRate}", 2)
epsilonInt = int(f"0b{epsilonRate}", 2)

powerConsumption = gammaInt * epsilonInt 

print(f"{gammaRate}")
print(f"{epsilonRate}")
print(f"{gammaInt}")
print(f"{epsilonInt}")
print(f"{powerConsumption}")