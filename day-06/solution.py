# Now that the supplies have been retrieved, the Elves have started to venture into the jungle.
# They are using a communication device to track a signal, and have given you a broken one.
# To fix it, you have to add a subroutine that detects the communication packets
# that mark the message.
# This packet is indicated by 4 contiguous letters in the stream that are different.
# Given a stream of data, return the amount of characters before the end of the first valid data packet
# is found.


input = open("input.txt", "r")
stream = input.read()
stream = stream.strip('\n')

# We can create a sliding window, where we can check against our
# constraint of 4 unique characters using a hm.
def getStreamLengthTillPacketSize(stream, packetSize):
    uniqs = {}
    for (i, char) in enumerate(stream):
        if i < packetSize:
            if (char in uniqs):
                uniqs[char] += 1
            else:
                uniqs[char] = 1
        else:
            removePointer = stream[i - packetSize]
            uniqs[removePointer] -= 1
            if (char in uniqs):
                uniqs[char] += 1
            else:
                uniqs[char] = 1
            listOfOnes = [one for one in list(uniqs.values()) if one == 1]
            print(uniqs)
            print(listOfOnes)
            if len(listOfOnes) == packetSize:
                return i + 1

print("Length of stream when end of first communications packet: ", getStreamLengthTillPacketSize(stream, 4))
#  --- Part 2 --- #
# The first message packet is identified by 14 distinct characters, when does this happen?
# These don't have to be in order.

print("Length of stream at end of first message packet: ", getStreamLengthTillPacketSize(stream, 14))



