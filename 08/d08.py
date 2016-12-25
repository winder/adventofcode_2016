#!/usr/bin/env python3
import sys
import re
import pprint
import operator
pp = pprint.PrettyPrinter(indent=4)

def printGrid(grid):
    w = len(grid[0])
    h = len(grid)
    # print("%d x %d" % (w, h))
    for y in range(0,h):
        for x in range(0,w):
            print(grid[y][x], end="")
        print("")

def rotate(l, x):
  return l[-x % len(l):] + l[:-x % len(l)]

def drawRect(grid, x, y):
    for xx in range(0,x):
        for yy in range(0,y):
            # print(str(xx) + " x " + str(yy))
            grid[yy][xx] = '#'

# offset in direction
# steps to rotate
def rotateColumn(grid, offset, steps):
    col = []
    length = len(grid)
    for i in range(length):
        col.append(grid[i][offset])

    col = rotate(col, steps)

    for i in range(length):
        grid[i][offset] = col[i]

def rotateRow(grid, offset, steps):
    length = len(grid[offset])
    grid[offset] = rotate(grid[offset], steps)

def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    filename = sys.argv[3]

    grid = [[' ' for x in range(width)] for y in range(height)] 

    Q1 = 0
    Q2 = 0
    for line in open(filename):
        # print("Line: %s" % line)
        matches = re.search("(.*?) (.*)", line)
        command = matches.group(1)
        args = matches.group(2)

        if command == "rect":
            matches = re.search("(\d+)x(\d+)", args)
            drawRect(grid, int(matches.group(1)), int(matches.group(2)))

        elif command == "rotate":
            matches = re.search("(\w+) \w=(\d+) by (\d+)", args)
            if matches.group(1) == "column":
                rotateColumn(grid, int(matches.group(2)), int(matches.group(3)))
            elif matches.group(1) == "row":
                rotateRow(grid, int(matches.group(2)), int(matches.group(3)))
            
        else:
            print("Unknown command '%s' on line '%s'." % (command,line))
        # printGrid(grid)

    Q1 = 0
    for x in range(width):
        for y in range(height):
            if grid[y][x] == '#':
                Q1 += 1

            
    print("Result Q1: %d" % Q1)
    print("Result Q2:")
    printGrid(grid)


if __name__ == "__main__":
    main()
