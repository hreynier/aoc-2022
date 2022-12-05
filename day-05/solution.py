import math
import re
# The elves have the rest of the supplies on crates marked with letters on their ship.
# These crates are stacked, and a crane operator can move each crate between the stacks one-by-one.
# The operator has a set of instructions of how to do this, moving X amount of crates from one stack to another.
# Even if 3 crates are moved from one stack, this is still done crate-by-crate, so the top crate is moved first.

#  --- Part 1 ---  #
# Return the top crates from each stack after the operator has finished moving each crate.
#  --- Part 2 --- #
# The crate can move all crates at once per instruction, meaning that crates aren't moved one-by-one. Update the
# final top crates.


# We first need to store the state of the crates and stacks as they are.
# Moving crates always takes the crate on top of the stack, so we can use array methods like pop and append
# to simulate this.

input = open("input.txt", "r")
lines = input.readlines()

# First we want to process the input file, assigning the original state of the supply ship to one structure
# And the instructions to another.
supplyShip = [[] for row in range(9)]
# Storing instructions as list, where first int is number of boxes, second is origin stack, third is destination stack
instructions = []
for line in lines:
    line = line.strip('\n')
    # 35 characters for each row of the ship, 3 for each crate and one gap between * 9 stacks = 35.
    if(len(line) > 34):
        divisor = 35/9
        for (i, char) in enumerate(line):
            if char.isalpha():
                stack = math.floor(i / divisor)
                supplyShip[stack].append(char)
    elif(len(line) > 1):
        instruction = re.split("move | from | to ", line)
        empty, *tail = instruction
        instruction = tail
        instructions.append(instruction)

for stack in supplyShip:
    stack.reverse()

# Now we can apply the instructions to the supply ship
#
# Part 1 Version 
# for instruction in instructions:
#     numberOfCrates = int(instruction[0])
#     origin = int(instruction[1]) - 1
#     destination = int(instruction[2]) - 1
#     while numberOfCrates > 0:
#         crate = supplyShip[origin].pop()
#         supplyShip[destination].append(crate)
#         numberOfCrates -= 1

# Part 2 Version
for instruction in instructions:
    numberOfCrates = int(instruction[0])
    origin = int(instruction[1]) - 1
    destination = int(instruction[2]) - 1
    movingStack = []
    while numberOfCrates > 0:
        crate = supplyShip[origin].pop()
        movingStack.append(crate)
        numberOfCrates -= 1
    movingStack.reverse()
    for crate in movingStack:
        supplyShip[destination].append(crate)

topCrates = []
for stk in supplyShip:
    top = stk.pop()
    topCrates.append(top)
    stk.append(top)

print("After operations, the top crates on each stack: ", topCrates)
