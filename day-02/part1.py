# To decide whose tent gets to be closest to the snack storage,
# the elves are conducting a Rock, Paper, Scissors tournement.
# We've been given a strategy guide that dictates us a strategy
# to win the tournement.
# Points are calculated as follows:
# 0 - Loss, 3 - Draw, 6 - Win
# 1 - Rock, 2 - Paper, 3 - Scissors
# The first column dictates the opponents position:
# A - Rock, B - Paper, C - Scissors
# The second dictates what we should play:
# X - Rock, Y - Paper, Z - Scissors
# Work out our total score if we were to follow the guide.

strategyGuide = open("input.txt", "r")
lines = strategyGuide.readlines()

# Returns the round score based on whether the round was won, lost or drawn.
def getRoundOutcomeScore(them, our):
    if (them == "A" and our == "Y") or (them == "B" and our == "Z") or (them == "C" and our == "X"):
        return 6
    elif (them == "A" and our == "X") or (them == "B" and our == "Y") or (them == "C" and our == "Z"):
        return 3
    else: return 0

def getRPSScore(whatWePlayed):
    if whatWePlayed == "X":
        return 1
    if whatWePlayed == "Y":
        return 2
    if whatWePlayed == "Z":
        return 3


score = 0
for round in lines:
    round = round.strip('\n')
    theirPick = round.split(" ")[0]
    ourPick = round.split(" ")[1]
    outcomeScore = getRoundOutcomeScore(theirPick, ourPick)
    playedScore = getRPSScore(ourPick)

    score = score + outcomeScore + playedScore
print("Total score after following strategy: ", score)