import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, '..'))
from aoc import run


def part1(data):
    lines = data.splitlines()
    pos = 0
    depth = 0

    for line in lines:
        op, n = line.split()
        n = int(n)
        if op[0] == 'f':
            pos += n
        elif op[0] == 'd':
            depth += n
        else:
            depth -= n

    return pos * depth


def part2(data):
    lines = data.splitlines()
    pos = 0
    aim = 0
    depth = 0

    for line in lines:
        op, n = line.split()
        n = int(n)
        if op[0] == 'f':
            pos += n
            depth += aim * n
        elif op[0] == 'd':
            # depth += n
            aim += n
        else:
            aim -= n
            # depth -= n

    return pos * depth

run(part1, part2, os.path.join(local_dir, "input.txt"))