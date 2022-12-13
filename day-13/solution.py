# After climbing the hill, you get a distress call from the Elves.
# Perhaps the device is malfunctioning, so you try to reorder the packets correctly to decode
# the message properly.
# The message contains packets as pairs separated by blank lines. you have to identify how many
# pairs of packets are in the right order.

# Packet data consists of lists and integers. Each list starts and ends with [ and ].
# When comparing two values, the first value is called left and second right.
# If both values are intergers, the lower int should come first.
# If they are equal, move to the next element in the packet, if the right is smaller then they are incorrect.
# If both values are lists, compre the first item in the list of the left to the first in the right.
# If the left list is smaller, they are correct.
# If exactly one value is an integer, convert it to a list and compare.

# What are the indices of the pairs that are in the right order?
# What is the sum of the indices of those pairs?

import numpy as np
from functools import cmp_to_key

with open("input.txt") as f:
    pairs = [[eval(l) for l in x.split()] for x in f.read().split("\n\n")]

print(pairs)

def is_pair_correct_order(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    if type(left) == list and type(right) == list:
        if len(left) == 0 and len(right) == 0:
            return 0
        if len(left) == 0: return -1
        if len(right) == 0: return 1
        r1 = is_pair_correct_order(left[0], right[0])
        return r1 if r1 != 0 else is_pair_correct_order(left[1:], right[1:])
    return is_pair_correct_order([left], right) if type(left) == int else is_pair_correct_order(left, [right])

sum = sum(i for i, (l, r) in enumerate(pairs, start = 1) if is_pair_correct_order(l, r) < 0)

print("sum of indices in correct order: ", sum)

# --- part 2 --- #

# You need to sort the correct packets as well as two additional divider packets
# [[2]] and [[6]]
# Return the indices of the divoer packets within the sorted packets and multiple them together.

pairs = np.array(pairs).flatten()
pairs = pairs.tolist()
pairs.extend([[[2]], [[6]]])
pairs_sorted = sorted(pairs, key=cmp_to_key(is_pair_correct_order))
i1, i2 = pairs_sorted.index([[2]]) + 1, pairs_sorted.index([[6]]) + 1
print("decoder: ", i1*i2)

