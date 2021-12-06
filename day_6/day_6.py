import sys
import os
from icecream import ic
from collections import defaultdict

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def calc_population(fish: list[int], days: int) -> int:
    pop: defaultdict[int, int] = defaultdict(int)
    for n in fish:
        pop[n] += 1

    for _ in range(days):
        new_pop = defaultdict(int)
        for k, v in pop.items():
            new_pop[k - 1] = v

        new_pop[8] = new_pop[-1]
        new_pop[6] += new_pop[-1]
        new_pop[-1] = 0

        pop = new_pop

    return sum(pop.values())


def part1(data: str):
    fish = list(map(int, data.split(",")))
    return calc_population(fish, 80)


def part2(data: str):
    fish = list(map(int, data.split(",")))
    return calc_population(fish, 256)


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """""")
