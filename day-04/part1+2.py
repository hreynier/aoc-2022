# Elves are assigned ids to clean sections of the camp.
# {
#    2-4,3-8
#   2-3,  5-6
# }
# Elf 1 is assigned 2,3,4, Elf 2, 3,4,5,7,8 etc.
# Some sections are entirely contained within another Elf's juristiction.
# Find how many assignment pairs does one range fully contain the other.

# Solution: Iterate through, take lowest number in pair, check if other number is highest.

file = open("input.txt", "r")
lines = file.read().splitlines()

def isContaining(a,b):
    return int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])

# --- Part Two --- #
# There is still a lot of duplicated work, so the elves want to know 
# all the pairs that overlap in any way.

def isOverlapping(a,b):
    return int(a[0]) >= int(b[0]) and int(a[0]) <= int(b[1])

totalOverlaps = 0
totalContains = 0
for pair in lines:
    pair = [section.split('-') for section in pair.strip('\n').split(',')]
    left, right = pair[0], pair[1]
    if isContaining(left, right) or isContaining(right, left):
        totalContains += 1
    if isOverlapping(left, right) or isOverlapping(right, left):
        totalOverlaps += 1

print("Total pairs where one fully contains the other's section assignment: ", totalContains)
print("Total pairs where they overlap in sections: ", totalOverlaps)