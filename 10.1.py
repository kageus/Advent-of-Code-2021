lineInput = open("./input/input_10.txt").read().split("\n")
scoreKey = {
    ")":     3,
    "]":    57,
    "}":  1197,
    ">": 25137
}
pairKeys = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
unresolvedOpen = []
score = 0
for line in lineInput:
    for x in range(0, len(line)):
        if line[x] in pairKeys.values():
            unresolvedOpen.append(line[x])
        elif line[x] in pairKeys.keys():
            if unresolvedOpen.pop() != pairKeys[line[x]]:
                score += scoreKey[line[x]]
                break
    unresolvedOpen.clear()
print(score)