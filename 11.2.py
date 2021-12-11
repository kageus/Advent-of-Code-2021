import numpy as np
lineInput = open("./input/input_11.txt").read().split("\n")
w, h = len(lineInput[0]), len(lineInput)
listInput = []
for line in lineInput:
    for character in line:
        listInput.append(int(character))
a = np.array(listInput).reshape(h, w)

def flasher(a, x, y, flashCount, flashed):
    flashCount += 1
    flashed.append((x, y))
    # up
    if y != 0                           and a[y-1][x] < 10:
        a[y-1][x] += 1
        if(a[y-1][x]) == 10:
            a, flashCount, flashed = flasher(a, x, y-1, flashCount, flashed)
    # up right
    if y != 0 and x < len(a[y])-1       and a[y-1][x+1] < 10:
        a[y-1][x+1] += 1
        if(a[y-1][x+1]) == 10:
            a, flashCount, flashed = flasher(a, x+1, y-1, flashCount, flashed)
    # right
    if x < len(a[y])-1                  and a[y][x+1] < 10:
        a[y][x+1] += 1
        if(a[y][x+1]) == 10:
            a, flashCount, flashed = flasher(a, x+1, y, flashCount, flashed)
    # down right
    if y < len(a)-1 and x < len(a[y])-1 and  a[y+1][x+1] < 10:
        a[y+1][x+1] += 1
        if(a[y+1][x+1]) == 10:
            a, flashCount, flashed = flasher(a, x+1, y+1, flashCount, flashed)
    # down
    if y < len(a)-1                     and  a[y+1][x] < 10:
        a[y+1][x] += 1
        if(a[y+1][x]) == 10:
            a, flashCount, flashed = flasher(a, x, y+1, flashCount, flashed)
    # down left
    if y < len(a)-1 and x != 0          and  a[y+1][x-1] < 10:
        a[y+1][x-1] += 1
        if(a[y+1][x-1]) == 10:
            a, flashCount, flashed = flasher(a, x-1, y+1, flashCount, flashed)
    # left
    if x != 0                           and a[y][x-1] < 10:
        a[y][x-1] +=1
        if(a[y][x-1]) == 10:
            a, flashCount, flashed = flasher(a, x-1, y, flashCount, flashed)
    # left up
    if x != 0 and y != 0                and a[y-1][x-1] < 10:
        a[y-1][x-1] += 1
        if(a[y-1][x-1]) == 10:
            a, flashCount, flashed = flasher(a, x-1, y-1, flashCount, flashed)
    return a, flashCount, flashed

flashCount = 0
flashed = []
steps = 0
# for i in range(0, steps):
while(not np.all(a == a[0][0])):
    a = a + 1
    toFlash = np.where(a > 9)
    for y, x in list(zip(toFlash[0], toFlash[1])):
        a, flashCount, flashed = flasher(a, x, y, flashCount, flashed)

    toZero = np.where(a > 9)
    for y, x in list(zip(toZero[0], toZero[1])):
        a[y][x] = 0
    steps += 1
    print(f"after step: {steps}\n{a}\n")
    


print(flashCount)

