# The elves have packed some backpacks of supplies but some items need
# to be rearranged. 
# Each backpack has two large compartments, and all items of a given type
# are meant to go into exactly one of the two compartments.
# Each item type is denoted by a single upper or lowercase letter (a-z, A-Z)
# And each backpack has the same number of items in each compartment,
# ex: {
#   vJrwpWtwJgWrhcsFMMfFFhFp
#   jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#   PmmdzqPrVvPwwTWBwg
#   wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#   ttgJtRGJQctTZtZT
#   CrZsJsPPZsGzwwsLwLmpwMDw
# }
# - First backpack first compartment -> vJrwpWtwJgWr, 2nd -> hcsFMMfFFhFp

# Each item type has a priority a -> z, 1 - 26, A -> Z 27 - 52.
# Find the item type that appears in both compartments for each backpack
# and return the sum of each of their priorities.

# Every three backpacks are grouped, find the priority for the shared item between them
# and the running total.

# ---- Solution ---- #
# Loop through input line by line, each line = a backpack.
# we can get length of each line and split in half by each compartment.
# We only want to find the letter that appears in both halfs, could do this with hashmap?
# Once we have this letter, we get it's priority using math and then add that to a running total.

file = open("input.txt", "r")
backpacks = file.readlines()

# We use the unicode values of the character to work out the priority
def getItemPriority(item):
    char = item.lower()
    val = ord(char) - ord("a") + 1
    return val + 26 if item.isupper() else val

def splitBackpackInChunks(backpack, numOfChunks):
    bpLen, compLen = len(backpack), len(backpack) // numOfChunks
    return [backpack[i:i+compLen] for i in range(0, bpLen, compLen)]

def findSharedItem(compartment1, compartment2):
    frequency = {}
    for char in compartment1:
        frequency[char] = 1
    for char in compartment2:
        if frequency.get(char) == 1:
            return char

def findSharedItemPriorityInBackpack(backpack):
    backpack = backpack.strip('\n')
    compartments = splitBackpackInChunks(backpack, 2)
    sharedItem = findSharedItem(compartments[0], compartments[1])
    val = getItemPriority(sharedItem)
    return val

def findElfGroupPriority(backpacks, i):
    groupedBackpacks = [bp.strip('\n') for bp in backpacks[i-2:i+1]]
    sharedItem = set(groupedBackpacks[0]).intersection(groupedBackpacks[1], groupedBackpacks[2]).pop()
    return getItemPriority(sharedItem)


totalPriority = 0
totalElfGroupPriority = 0
groupCount = 0

for (i,backpack) in enumerate(backpacks):
    groupCount += 1
    totalPriority += findSharedItemPriorityInBackpack(backpack)
    if groupCount > 2:
        elfGroupPriority = findElfGroupPriority(backpacks, i)
        totalElfGroupPriority += elfGroupPriority
        groupCount = 0


print("The total sum of shared items: ", totalPriority)
print("The total sum of priorities in groups: ", totalElfGroupPriority)
