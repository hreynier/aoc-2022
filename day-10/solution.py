# After falling into the river, your communication device is broken so you need to replace the video system.
# It seems to be some kind of Cathode Ray Tube and simple CPU that are driven by a precise clock circuit.
# The clock ticks at a constant rate, with each tick called a cycle.

# Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

    # addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
    # noop takes one cycle to complete. It has no other effect.

# The signal strength is determined by the cycle number times the value of the X register.

# --- Part 1 --- # 
# Find the signal strength at 20th, 60, 100, 140, 180, and 220th cycles. Return sum of these strengths.


file = open("input.txt", "r")
file = file.readlines()

# Store signal strengths in list.
signalStrengths = []
registerList = []
xRegister = 1
importantCycles = [20, 60, 100, 140, 180, 220]

for instruction in file:
    instruction = instruction.strip('\n')
    instruction = instruction.split(" ")
    currCycle = len(signalStrengths) + 1
    sigStrength = xRegister * currCycle
    if instruction[0] == "noop":
        signalStrengths.append(sigStrength)
        registerList.append(xRegister)
    elif instruction[0] == "addx":
        signalStrengths.append(sigStrength)
        registerList.append(xRegister)
        currCycle = len(signalStrengths) + 1
        sigStrength = xRegister * currCycle
        signalStrengths.append(sigStrength)
        registerList.append(xRegister)
        xRegister += int(instruction[1])


def sumOfValsAtIndices(arr, indexArr):
    sum = 0
    for el in indexArr:
        sum += arr[el-1]
    return sum

sumOfSpecificCycles = sumOfValsAtIndices(signalStrengths, importantCycles)

print("Sums of cycles at designated points: ", sumOfSpecificCycles)


# --- Part 2 --- #
# The X Register controls the horizontal position of the center of a 3-pixel wide sprite.
# The CRT screen is 40 wide and 6 high. It draws from the top row, left-to-right. The left-most pixel is 0
# and the right most is 39.


# The CRT draws a single pixel during each cycle. If the sprite is positioned such that one of it's 3 pixels is being
# drawn by the CRT, the CRT will render a `#` otherwise it will render a `.`.

CRT = []
pixelRow = []
for cycle in range(240):
    cyclePositionInRow = cycle % 40
    spriteCenter = registerList[cycle]
    pixel = ""
    if cyclePositionInRow >= (spriteCenter - 1) and cyclePositionInRow <= (spriteCenter + 1):
        pixel = "#"
    else:
        pixel = "."
    pixelRow.append(pixel)

    # End of the screen
    if cyclePositionInRow == 39:
        pixelRow.append('\n')
        pixelRow = ''.join(pixelRow)
        CRT.append(pixelRow)
        pixelRow = []

for line in CRT:
    print(line)

# ###.......#...####..##....##...##......
# ###.......#...####..##....##...##......
# ##...##.#....##........##........####...
# ###..##.#.##.....##....##...#......##...
# #....##....#....##..###.....#....#.##...
# #....#..####...#....##...##.#...........
# .##.....####...###........##...###.####.