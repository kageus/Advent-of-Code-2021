from functions import oxygen, carbondiox

dataInput = open("./input/input_3.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

bitCount    = len(lineList[0])
lineCount   = len(lineList)

oxygenRating        = oxygen.oxygenRate(lineList, 0)
carbonDioxRating    = carbondiox.carbonDioxRate(lineList, 0)

def binaryStringToInt(binaryString):
    return int(f"0b{binaryString}", 2)

lifeSupportRating = binaryStringToInt(carbonDioxRating[0]) * binaryStringToInt(oxygenRating[0])

print(f"{binaryStringToInt(oxygenRating[0])} * {binaryStringToInt(carbonDioxRating[0])} =")
print(f"{lifeSupportRating}")