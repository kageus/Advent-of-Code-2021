import re, sys
from functions import bingocard

dataInput = open("./input/input_4.txt").read().split("\n")

draws = dataInput.pop(0).split(',')
draws = [int(i) for i in draws]

bingoCards = []
bingoCard  = []

# extract the bingo cards
for line in dataInput:
    if(line == ""):
        if(bingoCard != []):
            bingoCards += [bingoCard]
        bingoCard = []
        continue
    # convert duplicate spaces into single spaces
    line = re.sub(' +',' ', line).strip().split(' ')
    line = [int(i) for i in line]
    bingoCard += [line]
# add the last bingoCard
bingoCards += [bingoCard]

# draw removing winning cards until last winning card is found
hits = []
# add draws to hit list one at a time
for draw in draws:
    hits.append(draw)

    # check for horizontal wins
    for bingoCard in bingoCards:
        for line in bingoCard:
            if all(hit in hits for hit in line):
                bingoCards.remove(bingoCard)
                if(len(bingoCards) == 0):
                    print(f"last card: horz winner: {line}")
                    print(f"final score: {bingocard.getFinalScore(bingoCard, hits)}")
                    sys.exit()
    # check for vertical wins
    for bingoCard in bingoCards:
        for x in range(0, len(line)):
            vertical = []
            for line in bingoCard:
                vertical.append(line[x])
            if all(hit in hits for hit in vertical):
                bingoCards.remove(bingoCard)
                if(len(bingoCards) == 0):
                    print(f"vert winner: {vertical}")
                    print(f"final score: {bingocard.getFinalScore(bingoCard, hits)}")
                    sys.exit()