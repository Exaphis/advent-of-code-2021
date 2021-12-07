import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    pos = list(map(int, data.split(",")))

    best_cost = float("inf")
    for i in range(min(pos), max(pos) + 1):
        cost = sum(abs(x - i) for x in pos)

        best_cost = min(cost, best_cost)

    return best_cost


def part2(data: str):
    pos = list(map(int, data.split(",")))

    best_cost = float("inf")
    for i in range(min(pos), max(pos) + 1):
        cost = 0
        for x in pos:
            dist = abs(x - i)
            cost += int(dist * (dist + 1) / 2)

        best_cost = min(cost, best_cost)

    return best_cost


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """16,1,2,0,4,2,7,1,2,14""")
