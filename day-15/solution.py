# You deploy some automated sensors through the cave system to detect the source of the distress signal.
# These sensors can only find the nearest beacon to them, so despite having a map of beacons
# You cant trust that these are the only beacons in the area.

# Based on where a sensor and it's beacon are, and knowing that sensors only report on the nearest beacon to them
# We can determine areas of the map where there are definitely no more beacons, and areas where there could be./
# Just scanning on row y=2000000, how many positons cannot contain a beacon?
import re
import time

coords = []
origin_and_bounds = []
filled = set()
targetLevel = 2000000
st = time.time()
with open("input.txt") as f:
    for x in f.read().split('\n'):
        if len(x):
            nums = [int(el) for el in re.findall(r'[-+]?[.]?[\d]+', x)]
            coords.append(nums)
            sX, sY, bX, bY = nums
            distance = abs(bY-sY) + abs(bX-sX)
            # We can work out the max distance in each direction from the sensor.
            maxY, maxX, minY, minX = sY + distance, sX + distance, sY - distance, sX - distance
            origin_and_bounds.append([(sX, sY), (sX, maxY), (maxX, sY), (sX, minY), (minX, sY)])
           

# With this, we can find out at what point out area crosses the target level
# We then have to find out how much further we go beyond that target level to find the height of a triangle
# with the base being the squares along the target level.
def fill_target_level(ogBndList ,setF, lvl):
    origin, u, r, d, l = ogBndList
    widthAcrossTargetLevel = 0
    diff = 0
    maxY, minY = u[1], d[1]
    oX,oY = origin[0], origin[1]
    if maxY >= lvl and oY < lvl:
        diff = maxY - lvl
        widthAcrossTargetLevel = diff * 2 + 1
    elif minY <= lvl and oY > lvl:
        diff = lvl - minY
        widthAcrossTargetLevel = diff * 2 + 1

    # We can work out how many coordinates fall along this base and add to filled.
    if widthAcrossTargetLevel != 0:
        dX = 0
        setF.add(oX)
        for _ in range(0, diff):
            dX += 1
            setF.add((oX+dX))
            setF.add((oX-dX))

filled = set()
for sensor in origin_and_bounds:
    fill_target_level(sensor, filled, targetLevel)
et = time.time()
print("Total coordinates scanned with no beacons at level %s: %s" % (targetLevel,len(filled) - 1))
print("Execution time P1: ", et - st, " seconds.")
# --- Part 2 --- #
# There is a distress signal coming from somewhere within the bounds of 0, 4000000 in x and y.
# Find it's coordinate and return it's tuning frequency/
# this is located by multiplying the x coordinate by 4000000 and adding the y coordinate

# Get bounds of each sensor at each y level.

def get_min(el):
    return el[0]

# Here we get the bounds of each sensor at a certain level of y.
def get_bounds_at_lvl(origin_bound_list, lvl, maxBounds):
    origin, u, _, d, _ = origin_bound_list
    widthAcrossTargetLevel = 0
    diff = 0
    maxY, minY = u[1], d[1]
    oX,oY = origin[0], origin[1]

    if maxY == lvl or minY == lvl:
        if oX >= 0 and oX <= maxBounds:
            return (oX, oX)
    if maxY >= lvl and oY <= lvl:
        diff = maxY - lvl
        widthAcrossTargetLevel = diff * 2 + 1
    elif minY <= lvl and oY >= lvl:
        diff = lvl - minY
        widthAcrossTargetLevel = diff * 2 + 1

    if widthAcrossTargetLevel != 0:
        left, right = oX - diff, oX + diff
        if left < 0:
            left = 0
        if right > maxBounds:
            right = maxBounds
        return (left, right)

# We loop through the bounds list, and check for any gaps in the overlaps of bounds.
def get_values_outside_bounds(boundsList):
    boundsList.sort(key = get_min)
    lower = boundsList[1][1]
    for i in range(1, len(boundsList)):
        prevBounds = boundsList[i - 1]
        bounds = boundsList[i]
        _,u1 = prevBounds
        l2,_ = bounds
        lower = max(u1, lower)
        if l2 - 1 > lower:
            return l2 - 1


filled = set()
maxBounds = 4000000
ansCoord = 0

# We go from the min bound in y, 0, to the max boundary.
# At each level, we want to get the bounds of each sensor in the x-plane
# We can then check that they are overlapping and if not return that x coordinate
# and then we know what y we are in so we return that.
for y in range(0, maxBounds + 1):
    boundList = []
    for sensor in origin_and_bounds:
        b = get_bounds_at_lvl(sensor, y, maxBounds)
        if b:
            boundList.append(b)
    if len(boundList) > 0:
        potentialAns = get_values_outside_bounds(boundList)
        if potentialAns:
            ansCoord = (potentialAns, y)
            break
print("part 2: find the coordinates of missing beacon across total sensor coverage.")
st = time.time()
print("coordinate: ", ansCoord)
tuningFreq = ansCoord[0] * maxBounds + ansCoord[1]
et = time.time()
print("tuning frequency: ", tuningFreq)
print("Execution time P2: ", et - st, " seconds.")