from functions import oxygen, carbondiox

dataInput = open("./input/input_3.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

bitCount = len(lineList[0])
lineCount = len(lineList)

oxygenRating = oxygen.oxygenRate(lineList, 0)
carbonDioxRating = carbondiox.carbonDioxRate(lineList, 0)

def binaryStringToInt(binaryString):
    return int(f"0b{binaryString}", 2)

lifeSupportRating = binaryStringToInt(carbonDioxRating[0]) * binaryStringToInt(oxygenRating[0])

print(f"{binaryStringToInt(oxygenRating[0])} * {binaryStringToInt(carbonDioxRating[0])} =")
print(f"{lifeSupportRating}")







# # epsilon is inverted gamma 
# for i in range(bitCount):
#     if gammaRate[i] == '1':
#         epsilonRate += '0'
#     else:
#         epsilonRate += '1'

# # convert to integers
# gammaInt   = int(f"0b{gammaRate}", 2)
# epsilonInt = int(f"0b{epsilonRate}", 2)

# powerConsumption = gammaInt * epsilonInt 


# print(f"{gammaInt}")
# print(f"{epsilonInt}")
# print(f"{powerConsumption}")

