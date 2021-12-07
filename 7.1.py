dataInput = open("./input/input_7.txt").read().split(",")
positions = [int(x) for x in dataInput]

high    = max(positions)
low     = min(positions)
delta   = int(0)
# our initial best is the worst
best    = len(positions) * (high - low )

# brute force
for i in range(low, high+1):
    for position in positions:
        delta += abs(position - i)
    if(delta < best):
        best = delta
    delta = 0

print(best)