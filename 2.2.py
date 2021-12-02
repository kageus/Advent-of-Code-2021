dataInput = open("./input/input_2.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

depth = 0
position = 0
aim = 0

for line in lineList:
    direction, amount = line.split(' ')    
    amount = int(amount)

    if direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount
    elif direction == 'forward':
        position += amount
        if aim != 0:
            depth += aim * amount

print(f"depth * position =  {depth * position}")
