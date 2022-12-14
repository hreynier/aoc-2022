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

minX, maxX = 1000, 0 
minY, maxY = 1000, 0 

scan = []
with open("input.txt") as f:
    for x in f.read().split("\n"):
        if len(x):
            line = []
            for p in x.replace('->','').split():
                p = p.split(',')
                minX = min(minX, int(p[0])) 
                maxX = max(maxX, int(p[0])) 
                minY = min(minY, int(p[1])) 
                maxY = max(maxY, int(p[1])) 
                coord = [int(p[0]), int(p[1])]
                line.append(coord)
            scan.append(line)

print("bounds: ", (minX, maxX), (minY, maxY))
map = [['.' for _ in range(minX-2, maxX+2)] for _ in range(0, maxY + 2)]

for line in scan:
    for i, coord in enumerate(line):
        if i != (len(line) - 1):
            nextCoord = line[i + 1]
            normalisedCol = coord[0] - minX + 2
            normalisedRow = coord[1]
            for col in range(coord[0], nextCoord[0]):
                col = col - minX + 2
                # print((normalisedRow, col))
                map[normalisedRow][col] = '#'
            for row in range(coord[1], nextCoord[1]):
                # print((row, normalisedCol))
                map[row][normalisedCol] = '#'
# print(map)
sandStart = 500 - minX + 2
map[0][sandStart] = '+'
pretty = ''
for row in map:
    line = ''.join(row)
    print(line)
    pretty.join(line + '\n')

print(pretty)

resting = 0

def move_sand(coordinate):
    global resting
    row = coordinate[0]
    col = coordinate[1]

    if (row == len(map) - 1 or
        (map[row-1][col] != '.' and col == 0) or
        (map[row-1][col] != '.' and map[row-1][col-1] != '.' and col == len(map[0]) - 1)):
        map[row][col] = '~'
        move_sand([0, sandStart])
    
    if map[row - 1][col] == '~':
        map[row][col] = '~'
        move_sand([0, sandStart])
    elif map[row - 1][col] == '.':
        map[row-1][col] = 'o'
        map[row][col] = '.'
        move_sand([row-1, col])
    elif map[row-1][col-1] == '~':
        map[row][col] = '~'
        if map[row-1][col+1] == '~':
            return resting
        move_sand([0, sandStart])
    elif map[row-1][col-1] == '.':
        map[row-1][col-1] = 'o'
        map[row][col] = '.'
        move_sand([row-1, col-1])
    elif map[row-1][col+1] == '.':
        map[row-1][col+1] = 'o'
        map[row][col] = '.'
        move_sand([row-1, col+1])
    else:
        resting += 1
        move_sand([0, sandStart])

restingNum = move_sand([0, sandStart])

print(restingNum)

