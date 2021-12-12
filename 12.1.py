from collections import defaultdict, Counter

# dictionary of connections stored as sets
d       = defaultdict(set)
visited = defaultdict(int)
count   = Counter()


print(visited)

lineInput = open("./input/test_12_c.txt").read().split("\n")
for line in lineInput:
    k, v = line.split("-")
    if v != 'start' and k != 'end':
        d[k].add(v)
    if k != 'start' and v != 'end':
        d[v].add(k)

def runConnections(k, count, visited, teststr):
    if k.islower() and visited[k] < 1:
        visited[k] += 1
    for n in d[k]:
        if n == 'end':
            # print(f"{teststr} - end")
            count[f"{teststr} - end"] += 1
            continue
        if n in visited.keys():
            continue
        else:
            runConnections(n, count, visited, f"{teststr} - {n}")
    if(k in visited.keys()):
        visited.pop(k)
    
for k in d['start']:
    # print(f"mapping {k} legs\n")
    teststr = f"{k}"
    runConnections(k, count, visited, teststr)
    visited.clear()

print(len(count))