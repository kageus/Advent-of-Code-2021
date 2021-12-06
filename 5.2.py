from collections import Counter
dataInput = open("./input/input_5.txt").read().split("\n")

c = Counter([])

for line in dataInput:
    start, end = line.split(" -> ")
    x1, y1 = [int(x) for x in start.split(",")]
    x2, y2 = [int(x) for x in   end.split(",")]

    # only parse the vert or horizontal lines
    if      x1 == x2:
        for y in range((y1 if y1 < y2 else y2), (y1 if y1 > y2 else y2) +1):
            c.update([f"{x1},{y}"])
    elif    y1 == y2:
        for x in range((x1 if x1 < x2 else x2), (x1 if x1 > x2 else x2) +1):
            c.update([f"{x},{y1}"])
    else:
        dx = []
        dy = []
        xmod = 1 if x1 < x2 else -1
        ymod = 1 if y1 < y2 else -1
        for x in range(x1, (x2 + xmod), xmod):
            dx += [x]
        for y in range(y1, (y2 + ymod), ymod):
            dy += [y]
        for i in range(0, abs(x1 - x2)+1 ):
            c.update([f"{dx[i]},{dy[i]}"])

count = sum(1 for i in c.values() if i > 1)
print(count)