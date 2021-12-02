dataInput = open("./input/input_2.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

depth = 0
position = 0

for line in lineList:
    direction, amount = line.split(' ')    
    amount = int(amount)

    if direction == 'forward':
        position += amount
    elif direction == 'up':
        depth -= amount
    elif direction == 'down':
        depth += amount

print(f"depth * position =  {depth * position}")
