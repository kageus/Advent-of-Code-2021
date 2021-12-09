from collections import defaultdict
lineInput = open("./input/input_8.txt").read().split("\n")

count = 0
for line in lineInput:
    patterns, output    = line.split(" | ")
    output              = output.split(" ")
    patterns            = patterns.split(" ")
    patterns.sort(key=len)

    # know 1, 7, 4 8
    decoderDict = defaultdict(str)
    decoderDict['1']    = patterns[0]
    decoderDict['7']    = patterns[1]
    decoderDict['4']    = patterns[2]
    decoderDict['8']    = patterns[9]
    
    unknown6List    = [patterns[6], patterns[7], patterns[8]]
    # solve for 9 first
    setUnion4_7 = set(decoderDict['4']) | set(decoderDict['7'])
    for v in unknown6List:
        if len(set(v) - setUnion4_7) == 1:
            decoderDict['9']    = v
            unknown6List.remove(v)
    # solve for 0 and 6
    for v in unknown6List:
        if len(set(v) & set(decoderDict['1'])) == 2:
            decoderDict['0']    = v
            unknown6List.remove(v)
            decoderDict['6']    = unknown6List[0]
            break

    unknown5List    = [patterns[3], patterns[4], patterns[5]]
    #solve for 2
    for v in unknown5List:
        if len(set(decoderDict['9']) - set(v)) == 2:
            decoderDict['2']    = v
            unknown5List.remove(v)
    # solve for 3 and 5
    for v in unknown5List:
        if len(set(v) & set(decoderDict['1'])) == 2:
            decoderDict['3']    = v
            unknown5List.remove(v)
            decoderDict['5']    = unknown5List[0]
            break
    
    decoded_output = ''
    decoderDict = dict([(value, int(key)) for key, value in decoderDict.items()])
    for o in output:
        for d in decoderDict:
            if set(d) == set(o):
                decoded_output += str(decoderDict[d])
     
    count += int(decoded_output)

print(count)
