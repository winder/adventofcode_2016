#!/usr/bin/python
import sys
import re
import pprint
import operator

filename = sys.argv[1]

pp = pprint.PrettyPrinter(indent=4)

def isValid(histogram, checksum):
    # sorted_histo = sorted(histogram.items(), key=operator.itemgetter(1), reverse=True)
    sorted_histo = sorted(histogram.items(), key=lambda x: (-x[1],x[0]))
    # print("histo len: %d" % len(sorted_histo))
    del sorted_histo[len(checksum):]
    frequent = {}
    for item in sorted_histo:
        frequent[item[0]] = item[1]

    # print("histo len: %d" % len(sorted_histo))
    # pp.pprint(sorted_histo)
    # pp.pprint(frequent)
    for ch in checksum:
        if not ch in frequent:
            # print ("%s not in histogram." % ch)
            return False
    return True

def shift(char, shift_count):
    num = ord(char)
    a = ord('a')
    z = ord('z')
    for i in range(0, shift_count):
        if num == z:
            num = a
        else:
            num += 1
    return chr(num)

def decrypt(string, shift_count):
    ret = ""

    for i in  string:
        if i == '-':
            ret += ' '
        else:
            ret += shift(i, shift_count)

    return ret

Q1 = 0
Q2 = 0
for line in open(filename):
    # print("Line: %s" % line)
    matches = re.search("(.*)-(\d+)\[(\w+)\]", line)

    sector_id = int(matches.group(2))
    checksum = matches.group(3)
    histo = {}
    for ch in matches.group(1).replace('-',''):
        if not ch in histo:
            histo[ch] = 0
        histo[ch] = histo[ch] + 1
        # pp.pprint(histo)
    if isValid(histo, checksum):
        Q1 = Q1 + sector_id
        result = decrypt(matches.group(1), sector_id)
        # pp.pprint(result)
        # print("Decrypted: %s" % result)
        if result == "northpole object storage":
            Q2 = sector_id

print("Result Q1: %d" % Q1)
print("Result Q2: %d" % Q2)


