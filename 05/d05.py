#!/usr/bin/python
import sys
import re
import pprint
import md5

filename = sys.argv[1]
with open(filename, 'r') as myfile:
    seed = myfile.read().replace('\n', '')

pp = pprint.PrettyPrinter(indent=4)

password1 = ""
password2 = "--------"
offset = 0

while len(password1) < 8 or '-' in password2:
    chk = md5.new(seed + str(offset)).hexdigest()
    # pp.pprint(chk)
    if chk.startswith("00000"):
        if len(password1) < 8:
            password1 += chk[5]
        idx = ord(chk[5]) - ord('0')
        if idx >= 0 and idx < 8 and password2[idx] == '-':
            password2 = password2[:idx] + chk[6] + password2[idx+1:]
            print("Q2: %s" % password2)
    offset += 1

print("Q1: %s" % password1)
print("Q2: %s" % password2)
