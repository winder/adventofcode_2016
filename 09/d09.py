#!/usr/bin/env python3
import sys
import re
import pprint
import operator
pp = pprint.PrettyPrinter(indent=4)

def decompress(line, recurse):
    idx = 0
    result = ""
    while idx < len(line):
        #print(idx)
        #print(len(result))
        match = re.match("(.*?)\((\d+)x(\d+)\)(.*)", line[idx:])
        if match is not None:
            # Add the unmatched parts.
            span = match.span(1)
            result += line[idx:idx+span[1]]

            # Update idx to data section.
            idx = idx + match.span(4)[0]

            # Grab data section
            width = int(match.group(2))
            data = line[idx:idx+width]
            if recurse:
                data = decompress(data, True)

            # Repeat data section
            count = int(match.group(3))
            while count > 0:
                result += data
                count -= 1
                
            # Move idx past data
            idx += width
        else:
            result += line[idx:]
            return result
    return result

def main():
    filename = sys.argv[1]

    Q1 = 0
    Q2 = 0
    for line in open(filename):
        string = decompress(line.strip(), False)
        Q1 += len(string)
        string = decompress(line.strip(), True)
        Q2 += len(string)

    print("Result Q1: %d" % Q1)
    print("Result Q2: %d" % Q2)


if __name__ == "__main__":
    main()
