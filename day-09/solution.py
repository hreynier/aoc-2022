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
        if not isTouching(headCoordinates, tailCoordinates):
            hx, hy = headCoordinates[0], headCoordinates[1]
            tx, ty = tailCoordinates[0], tailCoordinates[1]

            diff_x = 0 if hx == tx else (hx - tx) / abs(hx - tx) # We just want the direction not magnitude
            diff_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tailCoordinates = [tx+diff_x, ty+diff_y]
            visited.add((tailCoordinates[0], tailCoordinates[1]))

print("total visited coordinates by tail: ", len(visited))

# --- Part 2 --- #
# We now have the same instructions, but instead for a rope with 10 knots rather than 2.
rope = []
for i in range(10):
    rope.append([0,0])
visited = set(tuple(rope[0]))

for instruction in file:
    instruction = instruction.strip('\n')

    direction = instruction.split(' ')[0]
    magnitude = int(instruction.split(' ')[1])

    for _ in range(magnitude):
        rope[0] = move(rope[0], direction)
        for i in range(1,10):
            head = rope[i-1]
            tail = rope[i]
            if not isTouching(head, tail):
                hx, hy = head[0], head[1]
                tx, ty = tail[0], tail[1]

                diff_x = 0 if hx == tx else (hx - tx) / abs(hx - tx) # We just want the direction not magnitude
                diff_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                rope[i] = [tx+diff_x, ty+diff_y]
                if i == 9:
                    visited.add(tuple(rope[9]))

print("total visited coordinates by tail for 10 knot rope: ", len(visited))
    
