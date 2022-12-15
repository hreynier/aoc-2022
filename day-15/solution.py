# You deploy some automated sensors through the cave system to detect the source of the distress signal.
# These sensors can only find the nearest beacon to them, so despite having a map of beacons
# You cant trust that these are the only beacons in the area.

# Based on where a sensor and it's beacon are, and knowing that sensors only report on the nearest beacon to them
# We can determine areas of the map where there are definitely no more beacons, and areas where there could be./
# Just scanning on row y=2000000, how many positons cannot contain a beacon?
import re

coords = []
origin_and_bounds = []
filled = set()
targetLevel = 2000000
# targetLevel = 10

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
    else:
        return
    print("width across: ", widthAcrossTargetLevel)
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

print(len(filled) - 1)

# --- Part 2 --- #
# There is a distress signal coming from somewhere within the bounds of 0, 4000000 in x and y.
# Find it's coordinate and return it's tuning frequency/
# this is located by multiplying the x coordinate by 4000000 and adding the y coordinate

filled = set()
maxBounds = 4000000
for x in range(0, maxBounds + 1):
    print(x)
for sensor in origin_and_bounds:
    for x in range(0, maxBounds + 1):
        fill_target_level(sensor, filled, x)

print(len(filled) - 1)