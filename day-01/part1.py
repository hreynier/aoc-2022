# input.txt represents a list of the calories of the food carried
# by each Elf. Each Elf separates their own inventory from the previous
# Elf's inventory by a blank line.
# Find the Elf carrying the most calories and return the total calories that
# that Elf is carrying.

# Input file
input = open("input.txt", "r")
# Get lines
lines = input.readlines()

# Iterate through each line, summing each Elf's total calories
# and then push to a list at the end of each Elf.
# We can also work out the max calories as we go.
maxCalories = 0
currentCalories = 0
for i, line in enumerate(lines):
    calorie = line.strip('\n')
    if len(calorie) == 0 or i == (len(lines) - 1):
        maxCalories = max(maxCalories, currentCalories)
        currentCalories = 0
    else:
        currentCalories = currentCalories + int(calorie)
print("max calories: ", maxCalories)