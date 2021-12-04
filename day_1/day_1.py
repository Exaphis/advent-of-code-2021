import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data):
    nums = list(map(int, data.splitlines()))
    increased = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            increased += 1
    return increased


def part2(data):
    nums = list(map(int, data.splitlines()))
    window = []
    sums = []
    increased = 0
    for i in range(len(nums)):
        window.append(nums[i])
        if len(window) == 3:
            s = sum(window)

            if sums and s > sums[-1]:
                increased += 1
            sums.append(s)
            window.pop(0)
    return increased


run(part1, part2, os.path.join(local_dir, "input.txt"))
