# The communication device still has some issues. To install an update
# you need to clear some space on the device.
# After navigating through the device's file directories, you can see the
# sizes of some files.
# The input is a list of linux navigation commands (cd {folder}, ls, etc)
# and file information (name, file size).
# Using this list, we can determine the tree of files on the device
# and what files are good candidates to be deleted.

# --- Part 1 --- # 
# Find all the directories with a total size of at most 10000.
# Return the total sum of all of their sizes.

# When we pass the command `cd ..` we have reached the end of a branch
# We can pass the size up to the previous directory

from collections import defaultdict

file = open("input.txt", "r")
commands = file.read()
# Split by commands
commands = commands.splitlines()

allDirectories = defaultdict(int)
rootPath = []

for cmd in commands:
    # Each directory we enter, we add to the stack, each time we leave we pop off
    # This allows us to refer to the current path via the stack to calculate directory sizes.
    if "$ cd" in cmd and cmd != '$ cd ..':
        dirName = cmd.split(' ')[2]
        rootPath.append(dirName)
    elif cmd == "$ cd ..":
        rootPath.pop()
    elif cmd.split(' ')[0].isnumeric():
        size = cmd.split(' ')[0]
        allDirectories[tuple(rootPath)] += int(size)
        # We want to add this size to all parent directories
        parentPath = rootPath[:-1]
        while parentPath:
            allDirectories[tuple(parentPath)] += int(size)
            parentPath.pop()

print("all directories raw size: ", allDirectories)

sum_10k = 0
for k,v in allDirectories.items():
    if v < 100000:
        sum_10k += int(v)

print("total sum of all directories less than 100,000: ", sum_10k)

# --- Part 2 --- #
# Total disk space available : 70000000
# Unused disk space needed   : 30000000

# We need to find the total space used so far, and then find one directory that we can remove to get the desired free space.

total_used = allDirectories.get(tuple('/'))
total_left = 70000000 - int(total_used)
total_needed_to_remove = 30000000 - total_left
min_size_to_del = 70000000 # Set to total space
for k,v in allDirectories.items():
    if v > total_needed_to_remove:
        min_size_to_del = min(min_size_to_del, v)

print("minimum size of directory to remove to satisfy desired space: ", min_size_to_del)