# The strategy guide is actually telling us whether we need to win, lose, or draw
# rather than what we should pick.
# Return the total score if we now follow the strategy guide correctly.
# X - Lost, Y - Draw, Z - Win

strategyGuide = open("input.txt", "r")
lines = strategyGuide.readlines()

scoresPerTheirPick = {
    "A": [3, 4, 8],
    "B": [1, 5, 9],
    "C": [2, 6, 7],
}

def getRoundScore(theirPick, desiredOutcome):
    if desiredOutcome == "X":
        return scoresPerTheirPick[theirPick][0]
    elif desiredOutcome == "Y":
        return scoresPerTheirPick[theirPick][1]
    else:
        return scoresPerTheirPick[theirPick][2]

score = 0
for round in lines:
    round = round.strip('\n')
    theirPick = round.split(" ")[0]
    desiredOutcome = round.split(" ")[1]
    roundScore = getRoundScore(theirPick, desiredOutcome)

    score = score + roundScore
print("Total score after following strategy: ", score)