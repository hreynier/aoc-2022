# Whilst walking across a rope bridge, you decide to mentally model some rope mechanics to pass your time?
# If we have a rope with two ends, TAIL = T, and HEAD = H, the on a coordinate grid.
# The two ends can't be far apart, and should always be touching, which means either
# occupying the same coordinates, or 1 away in any directions (diagonals included).
# We are given a set of instructions that the head of the rope can move in
# knowing the above rules, can we model how the tail should move and then return the total
# count of coordinate spaces that the tail EVER touches (so only count once).

# The heads and tails are on the same coordinate to start.

# Set the starting coordinate as (0,0). We can store the visited coordinates in an object.

file = open("input.txt", "r")
file = file.readlines()
headCoordinates = [0,0]
tailCoordinates = [0,0]

def isTouching(head, tail):
    hx = head[0]
    tx = tail[0]
    hy = head[1]
    ty = tail[1]

    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1

def move(coord, direction):
    if direction == "R":
        coord[0] = coord[0] + 1
    elif direction == "L":
        coord[0] = coord[0] - 1
    elif direction == "U":
        coord[1] = coord[1] + 1
    elif direction == "D":
        coord[1] = coord[1] - 1
    return coord

visited = set()
visited.add((tailCoordinates[0], tailCoordinates[1]))

for instruction in file:
    instruction = instruction.strip('\n')

    direction = instruction.split(' ')[0]
    magnitude = int(instruction.split(' ')[1])

    for i in range(magnitude):
        headCoordinates = move(headCoordinates, direction)
        print(headCoordinates)
        if not isTouching(headCoordinates, tailCoordinates):
            hx, hy = headCoordinates[0], headCoordinates[1]
            tx, ty = tailCoordinates[0], tailCoordinates[1]

            diff_x = 0 if hx == tx else (hx - tx) / abs(hx - tx) # We just want the direction not magnitude
            diff_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tailCoordinates = [tx+diff_x, ty+diff_y]
            visited.add((tailCoordinates[0], tailCoordinates[1]))

print("total visited coordinates by tail: ", len(visited))

    
