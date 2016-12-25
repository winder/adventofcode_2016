#!/usr/bin/env python3
import sys
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)


def get_low(bots, bot_id):
    if len(bots[bot_id]) != 2:
        raise ValueError('Bot is empty, cannot get low')
    return bots[bot_id][0]


def get_high(bots, bot_id):
    if len(bots[bot_id]) != 2:
        raise ValueError('Bot is empty, cannot get low')
    return bots[bot_id][1]


def add_to_bots(bots, bot_id, value):
    if bot_id not in bots or len(bots[bot_id]) == 0:
        bots[bot_id] = [value]
    elif len(bots[bot_id]) == 1:
        if bots[bot_id][0] < value:
            bots[bot_id] = bots[bot_id] + [value]
        else:
            bots[bot_id] = [value] + bots[bot_id]
    else:
        raise ValueError('More than two values in a bot!')

    if 5 in bots[bot_id] and 2 in bots[bot_id]:
        print("TEST: bot #%d" % bot_id)
    if 61 in bots[bot_id] and 17 in bots[bot_id]:
        print("Q1: %d" % bot_id)


# [dest_low, dest_low_id, dest_high, dest_high_id]
def processInstruction(bots, outputs, instructions, bot_id):
    if len(bots[bot_id]) != 2:
        return

    instruction = instructions[bot_id]
    low = get_low(bots, bot_id)
    if instruction[0] == "output":
        outputs[instruction[1]] = low
    else:
        add_to_bots(bots, instruction[1], low)

    high = get_high(bots, bot_id)
    if instruction[2] == "output":
        outputs[instruction[3]] = high
    else:
        add_to_bots(bots, instruction[3], high)

    bots[bot_id] = []

    processInstruction(bots, outputs, instructions, instruction[1])
    processInstruction(bots, outputs, instructions, instruction[3])


def main():
    outputs = {}
    bots = {}
    filename = sys.argv[1]
    instructions = {}

    # Get instructions and initialize bots
    for line in open(filename):
        match = re.search("bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", line)
        if match is not None:
            source_id = int(match.group(1))
            if source_id not in bots:
                bots[source_id] = []
            dest_low = match.group(2)
            dest_low_id = int(match.group(3))
            dest_high = match.group(4)
            dest_high_id = int(match.group(5))
            instructions[source_id] = [dest_low, dest_low_id, dest_high, dest_high_id]

        match = re.search("value (\d+) goes to bot (\d+)", line)
        if match is not None:
            value = int(match.group(1))
            bot_num = int(match.group(2))
            add_to_bots(bots, bot_num, value)
            continue

    # Look for something with two microchips
    for key, value in bots.items():
        processInstruction(bots, outputs, instructions, key)

    print("Q2: %d" % (outputs[0] * outputs[1] * outputs[2]))


if __name__ == "__main__":
    main()
