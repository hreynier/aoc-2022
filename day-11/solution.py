# Some monkeys have stolen some items from your backpack.
# They pass the items between each other such that it's nearly impossible to get them back.
# The monkey's seem to pass the items between each other based on your perceived "worry" about each item.
# With this, you can establish some rules that the monkey's follow when passing items.


# --- part 1 --- #
# Find the two monkey's who handle the most items after 20 rounds.
# Multiply these two numbers(number of items handled) to find the "monkey business" metric.

# We have to go through the monkey's in order. There are seven monkey's, so each round should go through them one-by-one.
# If a monkey is holding no items when it's their turn, we can skip them.
# We first want to parse the input so that we have lists for each monkey.

import math
import copy


file = open("input.txt", "r")
file = file.readlines()

monkeys = {}

def createNewMonkey(monkeyName, lines, monkeyList):
    items = [int(el.strip(',')) for el in lines[1].strip('\n').split(" ")[4:]]
    operation = lines[2].strip('\n').split(" ")[-3:]
    divisor = int(lines[3].strip('\n').split(" ")[-1:].pop())
    trueMonkey = int(lines[4].strip('\n').split(" ")[-1:].pop())
    falseMonkey = int(lines[5].strip('\n').split(" ")[-1:].pop())
    monkey = {"name": monkeyName,"items": items,"operation": operation, "divisor": {"num": divisor, "true": trueMonkey, "false": falseMonkey}}
    monkeys[monkeyName] = monkey

for (i,line) in enumerate(file):
    line = line.strip('/n')
    line = line.split(" ")
    if line[0] == "Monkey":
        name = int(line[1].strip(':\n'))
        lines = file[i:i+6]
        createNewMonkey(name, lines, monkeys)

# Now go through monkeys round by round
def getMonkeyBusiness(monkeysObject, totalRounds, worryDivider):

    # If we are dealing with large rounds and numbers, we can't find the modulo of each integer quickly
    # So we want to first divide it by the lcm of each divisor -> 7,19,13,3,2,11,17,5
    # These are all prime numbers, so we times them together and divide the integer by this first.
    roundCount = 0
    monkeyCounts = [0 for _ in range(8)]
    lcm = 7*19*13*3*2*11*17*5

    while roundCount < totalRounds:
        for monKey, monkey in monkeysObject.items():
            print(monKey)
            itemsHandledThisRound = 0
            while len(monkey["items"]) > 0:
                itemsHandledThisRound += 1
                currItem = monkey["items"].pop(0)
                if monkey["operation"][1] == "+":
                    if monkey["operation"][2] == "old":
                        currItem += currItem
                    else:
                        currItem += int(monkey["operation"][2])
                else:
                    if monkey["operation"][2] == "old":
                        currItem = currItem * currItem
                    else:
                        currItem = currItem * int(monkey["operation"][2])
                if worryDivider != 1:
                    currItem = math.floor(currItem // worryDivider)
                else:
                    currItem %= lcm
                if currItem % monkey["divisor"]["num"] == 0:
                    monkeysObject[monkey["divisor"]["true"]]["items"].append(currItem)
                else:
                    monkeysObject[monkey["divisor"]["false"]]["items"].append(currItem)
            monkeyCounts[monKey] = monkeyCounts[monKey] + itemsHandledThisRound
        roundCount += 1
    monkeyCounts.sort()
    return monkeyCounts[6] * monkeyCounts[7]

monkeysCopy = copy.deepcopy(monkeys)
print(monkeysCopy)
monkeyBusinessP1 = getMonkeyBusiness(monkeys, 20, 3)
print("Monkey business in part 1: ", monkeyBusinessP1)
monkeyBusinessP2 = getMonkeyBusiness(monkeysCopy, 10000, 1)
print("Monkey business in part 2: ", monkeyBusinessP2)