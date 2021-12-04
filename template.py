import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    pass


def part2(data: str):
    pass


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """""")
