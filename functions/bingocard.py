def getFinalScore(bingoCard, hits):
    # unpack winning card
    winner = []
    for line in bingoCard:
        winner.extend(line)
    # remove hits from winner
    uncalledOnCard = [i for i in winner if i not in hits]
    # sum values left on card
    sumUncalled = sum(uncalledOnCard)
    # multiple sum by last hit
    return sumUncalled * hits[len(hits)-1]