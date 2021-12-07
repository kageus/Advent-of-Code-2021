from collections import defaultdict
dataInput = open("./input/input_7.txt").read().split(",")
positions = [int(x) for x in dataInput]

high        = max(positions)
low         = min(positions)

# dicitionary of distance costs
cost_dict = defaultdict(int)
cost = 0
for i in range(0, high+1):
    cost            += i
    cost_dict[i]    = cost 

# our initial best is the worst
best        = cost_dict[len(positions)] * (high - low )
this_cost   = int(0)

# brute force
for i in range(low, high +1):
    for position in positions:
        this_cost += cost_dict[abs(position - i)]
    if(this_cost < best):
        best = this_cost
    this_cost = 0

print(best)