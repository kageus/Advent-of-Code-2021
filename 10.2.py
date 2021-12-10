lineInput = open("./input/input_10.txt").read().split("\n")
scoreKey = {
    "(":     1,
    "[":     2,
    "{":     3,
    "<":     4
}
pairKeys = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
unresolvedOpen = []
score = 0
scores = []
corruptedLine = False

for line in lineInput:
    for x in range(0, len(line)):
        if line[x] in pairKeys.values():
            unresolvedOpen.append(line[x])
        elif line[x] in pairKeys.keys():
            if unresolvedOpen.pop() != pairKeys[line[x]]:
                corruptedLine = True
                break
    if corruptedLine:
        corruptedLine = False
        unresolvedOpen.clear()
        continue
    # resolve and score
    unresolvedOpen.reverse()
    for unresolved in unresolvedOpen:
        score *= 5
        score += scoreKey[unresolved]
    scores.append(score)
    score = 0
    unresolvedOpen.clear()
scores.sort()
print(scores[len(scores)//2])