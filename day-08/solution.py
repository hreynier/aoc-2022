# The expedition comes across a grid of trees that they want to build
# a treehouse in.
# The grid of trees is represented as a MxN grid (rows x col), where each tree
# has a height between 0 - 9.
# A tree is visible is if the trees next to it (up,right,left,down) have a lower height
# than it.

# --- Part 1 --- #
# How many trees are visible from outside the grid?
# All trees on the edge of the map are visible as there is nothing
# blocking their sight.

# As trees needs to have a clear line of sight from their position to the edge
# we can store the heighest 

import numpy as np

# Format map into MxN nested array grid
grid = []
file = open("input.txt", "r")
file = file.readlines()
for row in file:
    row = row.strip('\n')
    rowList = []
    for col in row:
        rowList.append(int(col))
    grid.append(rowList)

row_len = len(grid)
col_len = len(grid[0])

# Create numpy array, this allows us to check the heights along different axis
grid = np.array(grid)

# As we iterate through the grid, we need to check outwards in each direction from that tree
# If there are no trees that are taller than we can say that the tree is visible and increment our counter.

visible_trees = 0

for i in range(row_len):
    for j in range(col_len):
        currentHeight = grid[i, j]

        # If we are on left edge, or the max tree between left edge and tree is less than
        # tree height, tree is vis
        if j == 0 or np.amax(grid[i, :j]) < currentHeight:
            visible_trees += 1
        elif i == 0 or np.amax(grid[:i, j]) < currentHeight:
            visible_trees += 1
        elif j == col_len - 1 or np.amax(grid[i, (j+1):]) < currentHeight:
            visible_trees += 1
        elif i == row_len - 1 or np.amax(grid[(i+1):, j]) < currentHeight:
            visible_trees += 1


print("total visible trees: ", visible_trees)

# --- Part 2 --- #
# The elves want to build their tree house such that they can see the furthest from a tree, until the edge
# or another tree of the same height or higher is blocking.
# They are determining this from a scenic score, where each direction is multiplied.
# i.e, if they can see 4 trees north, 1 tree south, 2 trees west, and 1 tree east the score is
# 4 * 1 * 2 * 1 = 8

max_scenic_score = 0

for i in range(row_len):
    for j in range(col_len):
        currentHeight = grid[i, j]
        north = east = south = west = 0
        nHeight = eHeight = sHeight = wHeight = 0
        nLoc = sLoc = i
        eLoc = wLoc = j
        while nLoc > 0 and nHeight < currentHeight:
            nLoc -= 1
            nHeight = grid[nLoc, j]
            north += 1
        while sLoc < row_len - 1 and sHeight < currentHeight:
            sLoc += 1
            sHeight = grid[sLoc, j]
            south += 1
        while eLoc < col_len - 1 and eHeight < currentHeight:
            eLoc += 1
            eHeight = grid[i, eLoc]
            east += 1
        while wLoc > 0 and wHeight < currentHeight:
            wLoc -= 1
            wHeight = grid[i, wLoc]
            west += 1
        
        scenic_score = north * east * south * west
        max_scenic_score = max(max_scenic_score, scenic_score)

print("max scenic score on map: ", max_scenic_score)