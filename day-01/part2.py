# The Elves want to know the total calories carried by the top three
# elves instead.

# Input file
input = open("input.txt", "r")
# Get lines
lines = input.readlines()

# Iterate through each line, summing each Elf's total calories
# and then push to a list at the end of each Elf.
# We can then sort that list and return the top three summed.
caloriesPerElf = []
currentCalories = 0
totalTopCalories = 0
for i, line in enumerate(lines):
    calorie = line.strip('\n')
    if len(calorie) == 0 or i == (len(lines) - 1):
        caloriesPerElf.append(currentCalories)
        currentCalories = 0
    else:
        currentCalories = currentCalories + int(calorie)

caloriesPerElf.sort(reverse= True)
for x in range(3):
    totalTopCalories = caloriesPerElf[x] + totalTopCalories
print("Total calories carried by top three elves: ", totalTopCalories)
