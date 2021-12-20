import sys
import os
from typing import Generator
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run

P = tuple[int, int]


def get_neighbors(r: int, c: int) -> Generator[P, None, None]:
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            yield r + dr, c + dc


def enhance(pts: set[P], algo: str, off_in_pts: bool) -> tuple[bool, set[P]]:
    new_pts = set()

    consider: set[P] = set()
    for i, j in pts:
        consider.update(get_neighbors(i, j))

    if not off_in_pts:
        in_pts, out_pts = "1", "0"
        if algo[0] == "#":
            # all off turns into on
            # default should be on
            off_in_pts = True
    else:
        in_pts, out_pts = "0", "1"
        if algo[-1] == ".":
            # all on turns into off
            # default should be off
            off_in_pts = False

    for pt in consider:
        index_b = "".join(
            in_pts if (r, c) in pts else out_pts for r, c in get_neighbors(*pt)
        )
        index = int(index_b, 2)

        if not off_in_pts and algo[index] == "#":
            new_pts.add(pt)
        elif off_in_pts and algo[index] == ".":
            new_pts.add(pt)

    return off_in_pts, new_pts


def print_pts(pts: set[P]) -> None:
    min_row = min(r for r, _ in pts)
    min_col = min(c for _, c in pts)
    rows = max(r for r, _ in pts) - min_row
    cols = max(c for _, c in pts) - min_col

    grid = [["."] * (cols + 1) for _ in range(rows + 1)]
    for r, c in pts:
        grid[r - min_row][c - min_col] = "#"

    for row in grid:
        print("".join(row))


def part1(data: str):
    l = data.splitlines()
    algo = l.pop(0)
    assert len(algo) == 512
    l.pop(0)

    pts = set()
    for i, line in enumerate(l):
        for j, c in enumerate(line):
            if c == "#":
                pts.add((i, j))

    off_in_pts = False
    for _ in range(2):
        off_in_pts, pts = enhance(pts, algo, off_in_pts)

    return len(pts)


def part2(data: str):
    l = data.splitlines()
    algo = l.pop(0)
    l.pop(0)

    pts = set()
    for i, line in enumerate(l):
        for j, c in enumerate(line):
            if c == "#":
                pts.add((i, j))

    off_in_pts = False
    for _ in range(50):
        off_in_pts, pts = enhance(pts, algo, off_in_pts)

    return len(pts)


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# #..#.
# #....
# ##..#
# ..#..
# ..###""",
# )
