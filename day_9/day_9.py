import sys
import os
from collections import defaultdict
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def get_neighbors(r, c, arr):
    d = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for dr, dc in d:
        if 0 <= r + dr < len(arr) and 0 <= c + dc < len(arr[0]):
            yield r + dr, c + dc


def part1(data: str):
    arr = [list(map(int, line)) for line in data.split()]
    out = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            neighbors = [arr[nr][nc] for nr, nc in get_neighbors(r, c, arr)]
            if all(arr[r][c] < n for n in neighbors):
                out += arr[r][c] + 1

    return out


def part2(data: str):
    def get_low_point(r, c, arr):
        curr = (r, c)
        while True:
            neighbors = list(get_neighbors(curr[0], curr[1], arr))
            lowest = min(neighbors, key=lambda n: arr[n[0]][n[1]])
            if arr[lowest[0]][lowest[1]] >= arr[curr[0]][curr[1]]:
                return curr

            curr = lowest

    arr = [list(map(int, line)) for line in data.split()]
    basins = defaultdict(list)
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == 9:
                continue
            basins[get_low_point(r, c, arr)].append((r, c))

    lens = [len(b) for b in basins.values()]
    lens.sort(reverse=True)
    # ic(basins)
    # ic(lens)
    return lens[0] * lens[1] * lens[2]


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""",
# )
