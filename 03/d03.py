#!/usr/bin/python
import sys
import re

def possible(s1, s2, s3):
    #print("%3d %3d %3d" % (s1, s2, s3))
    largest=max(s1, s2, s3)
    remainder=s1 + s2 + s3 - largest

    # Check horizontally for Q1
    if (largest < remainder):
        return True
    return False

filename = sys.argv[1]

possibleQ1 = 0
possibleQ2 = 0
groups=[]
for line in open(filename):
    # Get row and convert to integers
    tail = [int(i) for i in re.search("\s*(\d+)\s+(\d+)\s+(\d+)", line).groups()]
    groups.append(tail)

    # Check horizontally for Q1
    if possible(tail[0], tail[1], tail[2]):
        possibleQ1 += 1

    # Check vertically for Q2
    if len(groups) == 3:
        for i in range(3):
            if possible(groups[0][i], groups[1][i], groups[2][i]):
                possibleQ2 += 1
        groups=[]

    #print(line)
print("Q1: %d" % possibleQ1)
print("Q2: %d" % possibleQ2)
