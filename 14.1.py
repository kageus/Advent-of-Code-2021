from collections import defaultdict, Counter
import time
lineInput = open("./input/test_14.txt").read().split("\n")

chain = lineInput.pop(0)
lineInput.pop(0)

pairDict = defaultdict(str)
for line in lineInput:
    k, v = line.split(" -> ")
    pairDict[k] = v

chains = []
c = Counter()

# not scalable with exponential growth
nextChain = chain[0]
steps = 10
for s in range(0, steps):
    
    c.clear()
    start = time.time()

    for i in range(0, len(chain)-1):
        nextChain += pairDict[chain[i:i+2]] + chain[i+1]
    
    end = time.time()
    
    for char in nextChain:
        c.update(char)
    
    print(chain)
    print(f"\nstep: {s+1} length: {len(chain)}  time:  {end - start}\n")
    print(c)
    
    chain = nextChain
    nextChain = chain[0]
    
solution = list(c.values())
solution.sort(reverse=True)
print(f"{solution[0]} - {solution[-1]} = {solution[0] - solution[-1]}")