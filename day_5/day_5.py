import sys
import os
from icecream import ic
from functools import cache

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


@cache
def get_pts(pt1, pt2):
    x = pt1[0]
    y = pt1[1]

    pts = {(x, y)}
    while (x, y) != pt2:
        if x != pt2[0]:
            x += 1 if x < pt2[0] else -1

        if y != pt2[1]:
            y += 1 if y < pt2[1] else -1
        pts.add((x, y))

    return pts


def get_overlap(pt1_1, pt1_2, pt2_1, pt2_2):
    pts_1 = get_pts(pt1_1, pt1_2)
    pts_2 = get_pts(pt2_1, pt2_2)
    return pts_1 & pts_2


def part1(data: str):
    lines = []
    for line in data.splitlines():
        pt1, pt2 = line.split(" -> ")
        pt1t = tuple(map(int, pt1.split(",")))
        pt2t = tuple(map(int, pt2.split(",")))

        if pt1t > pt2t:
            pt1t, pt2t = pt2t, pt1t

        if pt1t[0] == pt2t[0] or pt1t[1] == pt2t[1]:
            lines.append((pt1t, pt2t))

    overlaps = set()
    for i in range(1, len(lines)):
        for j in range(i):
            pt1_1, pt1_2 = lines[i]
            pt2_1, pt2_2 = lines[j]

            overlap = get_overlap(pt1_1, pt1_2, pt2_1, pt2_2)
            overlaps.update(overlap)

    return len(overlaps)


def part2(data: str):
    lines = []
    for line in data.splitlines():
        pt1, pt2 = line.split(" -> ")
        pt1t = tuple(map(int, pt1.split(",")))
        pt2t = tuple(map(int, pt2.split(",")))

        if pt1t > pt2t:
            pt1t, pt2t = pt2t, pt1t
        lines.append((pt1t, pt2t))

    overlaps = set()
    for i in range(1, len(lines)):
        for j in range(i):
            pt1_1, pt1_2 = lines[i]
            pt2_1, pt2_2 = lines[j]

            overlap = get_overlap(pt1_1, pt1_2, pt2_1, pt2_2)
            overlaps.update(overlap)

    return len(overlaps)


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""",
# )
