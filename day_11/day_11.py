import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def get_neighbors(r, c, arr):
    for dr, dc in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        if 0 <= r + dr < len(arr) and 0 <= c + dc < len(arr[0]):
            yield (r + dr, c + dc)


def part1(data: str):
    lvls = [list(map(int, line)) for line in data.split()]

    flashes = 0
    for i in range(100):
        s = set()

        flashed = set()
        for r in range(len(lvls)):
            for c in range(len(lvls[0])):
                lvls[r][c] += 1

                if lvls[r][c] > 9:
                    flashed.add((r, c))

        while flashed:
            s.update(flashed)
            # ic(i, s)
            new_flashed = set()

            for r, c in flashed:
                for dr, dc in get_neighbors(r, c, lvls):
                    lvls[dr][dc] += 1
                    if (
                        lvls[dr][dc] > 9
                        and (dr, dc) not in s
                        and (dr, dc) not in new_flashed
                    ):
                        new_flashed.add((dr, dc))

            flashed = new_flashed

        flashes += len(s)
        for r, c in s:
            lvls[r][c] = 0
        # ic(i, lvls)

    return flashes


def part2(data: str):
    lvls = [list(map(int, line)) for line in data.split()]

    for i in range(1000000):
        s = set()

        flashed = set()
        for r in range(len(lvls)):
            for c in range(len(lvls[0])):
                lvls[r][c] += 1

                if lvls[r][c] > 9:
                    flashed.add((r, c))

        while flashed:
            s.update(flashed)
            # ic(i, s)
            new_flashed = set()

            for r, c in flashed:
                for dr, dc in get_neighbors(r, c, lvls):
                    lvls[dr][dc] += 1
                    if (
                        lvls[dr][dc] > 9
                        and (dr, dc) not in s
                        and (dr, dc) not in new_flashed
                    ):
                        new_flashed.add((dr, dc))

            flashed = new_flashed

        for r, c in s:
            lvls[r][c] = 0

        if len(s) == len(lvls) * len(lvls[0]):
            return i + 1
    return None


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""",
# )
# run(
#     part1,
#     part2,
#     """11111
# 19991
# 19191
# 19991
# 11111""",
# )
