# Now that we have retrieved our items, we try to find the Elves using the handheld device.
# We seem to lose signal in the river valley, so we get a heightmap of the surrounding area
# to navigate to higher ground.

# The heightmap is delivered as a grid, with each square giving the elevation by a single lower case letter.
# a is the lowest, and z is the highest.
# Current location is at S, with the best location to get signal marked as E.
# You can move exactly one square in either direction, <- -> ^ \/
# You can only move up one elevation but can move down however many you like, meaning if you are at 
# square m you can go to n but not o.

# What is the fewest steps that you can move from your current position to the location with the best signal.

# Use a BFS algorithm, counting each step, returning when reaching the end goal.
# We can easily compare letters in python, so we just need to parse the input to a nested array.

input = open("input.txt", "r")
M = input.read().splitlines()

start = 0
startE = 0

for i,rows in enumerate(M):
    for j,letter in enumerate(rows):
        if letter == "S":
            start = [i,j]
        elif letter == "E":
            startE = [i,j]


def getValue(grid, row, col):
    value = grid[row][col]
    value = 'z' if value == 'E' else value
    value = 'a' if value == 'S' else value
    return value

def isValid(grid, coord, startCoord, visited):
    rowL = len(grid)
    colL = len(grid[0])
    row = coord[0]
    col= coord[1]
    if row >= 0 and row < rowL and col >= 0 and col < colL:
        value = getValue(grid, row, col)
        startValue = getValue(grid, startCoord[0], startCoord[1])
        value = ord(value) - 96
        startValue = ord(startValue) - 96
        tup = (row, col)
        return value - startValue < 2  and tup not in visited
    else: return False

def isReverseValid(grid, coord, startCoord, visited):
    rowL = len(grid)
    colL = len(grid[0])
    row = coord[0]
    col= coord[1]
    if row >= 0 and row < rowL and col >= 0 and col < colL:
        value = getValue(grid, row, col)
        startValue = getValue(grid, startCoord[0], startCoord[1])
        value = ord(value) - 96
        startValue = ord(startValue) - 96
        tup = (row, col)
        return startValue - value < 2  and tup not in visited
    else: return False

visit = {(start[0], start[1])}

def bfs(startCoordinates, endValue, visited):
    stepCount = -1
    queue = [startCoordinates]
    while len(queue) > 0:
        q = len(queue)
        nextQ = []
        stepCount += 1
        for i in range(q):
            coord =  queue[i]
            row = coord[0]
            col = coord[1]
            value = M[row][col]
            if value == endValue:
                return stepCount
            leftCol = col - 1
            rightCol = col + 1
            upRow = row + 1
            downRow = row - 1
            left = [row, leftCol]
            right = [row, rightCol]
            up = [upRow, col]
            down = [downRow, col]
            possDirections = [left, right, up, down]
            for dir in possDirections:
                valid = isValid(M, dir, coord, visited)
                if endValue == "a":
                    valid = isReverseValid(M, dir, coord, visited)
                if valid:
                    visited.add((dir[0], dir[1]))
                    nextQ.append(dir)
        print("Step count: ", stepCount)
        queue = nextQ

fastestStepsTillEnd = bfs(start, "E", visit)

print("fastest steps: ", fastestStepsTillEnd)

# --- Part 2 --- #
# You reckon the elves will want to turn this into a hiking trail, so we now want to find the shortest path
# from the highest point E 'z', to any lowest point 'a'.
    
visit = {(startE[0], startE[1])}
fastestStepsTillLowest = bfs(startE, "a", visit)

print("fastest steps till lowest: ", fastestStepsTillLowest)           