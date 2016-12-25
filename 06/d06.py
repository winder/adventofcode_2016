#!/usr/bin/python
import sys
import re
import pprint
import operator

filename = sys.argv[1]

pp = pprint.PrettyPrinter(indent=4)

frequencies = {}

num = 0

for line in open(filename):
    i = 0
    for ch in line.strip():
        if not i in frequencies:
            frequencies[i] = {}
        if not ch in frequencies[i]:
            frequencies[i][ch] = 0
        frequencies[i][ch] += 1
        i += 1
    if i > num:
        num = i

Q1 = ""
Q2 = ""
# pp.pprint(frequencies)
for i in range(num):
    spot = sorted(frequencies[i].items(), key=lambda x: (x[1]), reverse=True)
    Q1 += spot[0][0]
    Q2 += spot[-1][0]

print("Result Q1: %s" % Q1)
print("Result Q2: %s" % Q2)
