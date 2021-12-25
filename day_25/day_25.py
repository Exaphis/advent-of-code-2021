import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    d = data.splitlines()
    rows = len(d)
    cols = len(d[0])

    right = []
    down = []
    for r in range(rows):
        for c in range(cols):
            if d[r][c] == ">":
                right.append((r, c))
            elif d[r][c] == "v":
                down.append((r, c))

    cnt = 1
    while True:
        ex = set(right + down)

        moved = False
        nright = []
        for r, c in right:
            nr, nc = r, (c + 1) % cols
            if (nr, nc) in ex:
                nright.append((r, c))
                continue

            moved = True
            nright.append((nr, nc))

        for r, c in right:
            ex.remove((r, c))
        ex.update(nright)

        ndown = []
        for r, c in down:
            nr, nc = (r + 1) % rows, c
            if (nr, nc) in ex:
                ndown.append((r, c))
                continue

            moved = True
            ndown.append((nr, nc))

        right = nright
        down = ndown

        if not moved:
            break

        cnt += 1

    return cnt


def part2(data: str):
    pass


run(part1, part2, os.path.join(local_dir, "input.txt"))
