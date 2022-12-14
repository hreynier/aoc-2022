# The distress signal leads to a giant waterfall, with a large cave system behind it.
# As you enter the cave, you hear a rumbling as sand begins to rush into the cave.
# You scan a two-dimensional vertical slice of the cave above you and discover that it's mostly air
# with structures made of rock.

# Scan traces the path of each solid rock structure, reporting the x, y coordinates that form the shape of the
# rock.
# x is the distance to the right, y is the distance down.
# After the first point in the path, each point indicates the end of a straight horizontal or vertical line.
# 
# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# this indicates two paths of rock, first with two straight lines the second with three.
# sand pours into the cave at 500,0.
# Drawing rock as #, air as ., and the source of the sand as +, this becomes:

#   4     5  5
#   9     0  0
#   4     0  3
# 0 ......+...
# 1 ..........
# 2 ..........
# 3 ..........
# 4 ....#...##
# 5 ....#...#.
# 6 ..###...#.
# 7 ........#.
# 8 ........#.
# 9 #########.

# Sand is produced one unit at a time, and the next unit of sand is not produced
# until the previous unit of sand comes to rest.

# A unit of sand always falls down one step if possible.
# If the tile immediately below is blocked (by rock or sand), 
# the unit of sand attempts to instead move diagonally one step down and to the left. 
# If that tile is blocked, the unit of sand attempts to instead move diagonally one step down 
# and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, 
# then down-left, then down-right. If all three possible destinations are blocked, 
# the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ...o#ooo#.
# ..###ooo#.
# ....oooo#.
# .o.ooooo#.
# #########.

# Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom into the void.

# How many units of sand come to rest before sand starts flowing into the abyss below?

maxY = 0 

scan = []
with open("input.txt") as f:
    for x in f.read().split("\n"):
        if len(x):
            line = []
            for p in x.replace('->','').split():
                p = p.split(',')
                maxY = max(maxY, int(p[1])) 
                coord = [int(p[0]), int(p[1])]
                line.append(coord)
            scan.append(line)

# We can use a set so that we don't have to worry about the bounds of an array.

def add_to_set(prevCoord, coord, filled):
    x, y = prevCoord[0], prevCoord[1]
    dX, dY = coord[0], coord[1]

    for col in range(min(x, dX), max(x, dX) + 1):
        filled.add((y, col))
    for row in range(min(y, dY), max(y, dY) + 1):
        filled.add((row, x))

def set_stone_structures(scanArray):
    filled = set()
    for line in scanArray:
        for i in range(1,len(line)):
            coord = line[i]
            prevCoord = line[i - 1]
            add_to_set(prevCoord, coord, filled)
    return filled

def sim_sand(filled, maxY, sandStart):
    col, row = sandStart

    while row <= maxY:
        # Break when we reach the source sand.
        if(row, col) in filled:
            return False

        if (row + 1, col) not in filled:
            row += 1
            continue
        if (row + 1, col - 1) not in filled:
            col -= 1
            row += 1
            continue
        if (row + 1, col + 1) not in filled:
            col += 1
            row +=1
            continue
        
        # Grain is at rest
        filled.add((row, col))
        return True
    return False

# Set the stone structures into our set
filled = set_stone_structures(scan)
sandStart = (500, 0)
ans = 0
while True:
    sim = sim_sand(filled, maxY, sandStart)
    if not sim:
        break
    ans += 1
print("P1, Number of sands at rest after reaching stable state: ", ans)

# --- Part 2 --- #
# You now know that there is a floor beneath the stone structure, two levels beneath the lowest stone structure.
# Assuming the floor is infinetly long horizontally, how many sand grains will come to rest given that the flow stops
# once the sand reaches the top of the source at (0,500)?

# We can reuse our filled array, but instead pass a larger maxY to our simulation.
# We also have to add a break condition, when we reach the top of the sand source, at (0,500).

def set_stone_structure_with_floor(scan, floorLevel):
    filled = set_stone_structures(scan)
    for x in range(0,1000):
        filled.add((floorLevel, x))
    return filled

filled2 = set_stone_structure_with_floor(scan, maxY + 2)
ans = 0
while True:
    sim = sim_sand(filled2, maxY + 2, sandStart)
    if not sim:
        break
    ans += 1
print("P2, Number of sands at rest after reaching stable state: ", ans)