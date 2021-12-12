from collections import defaultdict, Counter

# dictionary of connections stored as sets
d       = defaultdict(set)
visited = defaultdict(int)
count   = Counter()

lineInput = open("./input/input_12.txt").read().split("\n")
for line in lineInput:
    k, v = line.split("-")
    if v != 'start' and k != 'end':
        d[k].add(v)
    if k != 'start' and v != 'end':
        d[v].add(k)

def runConnections(k, count, visited, teststr):
    
    if k.islower() and visited[k] < 1:
        visited[k] += 1
    elif k.islower() and set(visited.values()) == {1} :
        visited[k] += 1
    for n in d[k]:
        if n == 'end':
            # print(f"{teststr} - end")
            count[f"{teststr} - end"] += 1
            continue
        if n.islower() and n in visited.keys() and 2 in set(visited.values()):
            continue
        else:
            runConnections(n, count, visited, f"{teststr} - {n}")
    if(k in visited.keys()):
        if visited[k] == 2:
            visited[k] -= 1
        else:
            visited.pop(k)
    
for k in d['start']:
    # print(f"mapping {k} legs\n")
    teststr = f"{k}"
    runConnections(k, count, visited, teststr)
    visited.clear()

print(len(count))