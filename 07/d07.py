#!/usr/bin/python
import sys
import re
import pprint
import operator
from sets import Set

filename = sys.argv[1]

pp = pprint.PrettyPrinter(indent=4)

def supports(string):
    TLS = None
    supernet = Set([])
    hypernet = Set([])
    inBrackets = False
    length = len(string)
    for i in range(length):
        if string[i] == '[':
            inBrackets = True
        elif string[i] == ']':
            inBrackets = False
        else:
            if i+3 < length and string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
                # print("Found '%s' in %s" % (string[i:i+4], string))
                if inBrackets:
                    TLS = False
                elif TLS is None:
                    TLS = True
            elif i+2 < length and string[i] == string[i+2] and string[i] != string[i+1]:
                three = string[i] + string[i+1]
                if '[' not in three and ']' not in three:
                    if inBrackets:
                        supernet.add(three)
                    else:
                        hypernet.add(three)
    SSL = False
    for three in supernet:
        if three[1] + three[0] in hypernet:
            SSL = True

    return (TLS, SSL)

Q1 = 0
Q2 = 0
for line in open(filename):
    support = supports(line)
    if (support[0]):
        Q1 += 1
    if (support[1]):
        Q2 += 1

print("Result Q1: %d" % Q1)
print("Result Q2: %d" % Q2)


