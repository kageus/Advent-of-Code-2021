lineInput = open("./input/input_8.txt").read().split("\n")

lengthDict = { 2:1, 3:7, 4:4, 7:8 }
count = 0
for line in lineInput:
    patterns, output = line.split(" | ")
    digits = output.split(" ")
    for digit in digits:
        if len(digit) in lengthDict.keys():
            count += 1
print(count)
