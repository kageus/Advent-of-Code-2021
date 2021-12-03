def carbonDioxRate(lineList, currentIndex):

    onesCount = 0
    for line in lineList:
        bit = line[currentIndex]
        if bit == '1':
            onesCount += 1

    # create a new list that only contains the lines with the most common bit value
    if onesCount < len(lineList) - onesCount:
        reducedList = [line for line in lineList if line[currentIndex] == '1']
    else:
        reducedList = [line for line in lineList if line[currentIndex] == '0']

    # if reduced list has only 1 value return it
    if len(reducedList) == 1:
        pass
    # otherwise call oxygenRate again passing the reduced list and the next index to filter by
    else:
        reducedList = carbonDioxRate(reducedList, currentIndex + 1)

    return reducedList