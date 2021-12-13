import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    lines = data.splitlines()
    pts = []
    while lines[0]:
        pts.append(tuple(map(int, lines.pop(0).split(","))))
    lines.pop(0)

    nc = max(x[0] for x in pts)
    nr = max(x[1] for x in pts)

    paper = [[0] * (nc + 1) for _ in range(nr + 1)]
    for x, y in pts:
        paper[y][x] = 1

    for instr in [lines[0]]:
        if "x" in instr:
            col = int(instr[instr.index("=") + 1 :])
            for i in range(nr + 1):
                for j in range(col + 1, nc + 1):
                    if col - (j - col) < 0:
                        break

                    paper[i][col - (j - col)] |= paper[i][j]

                paper[i] = paper[i][: col + 1]
            nc = col + 1

    s = sum(x for row in paper for x in row)

    return s


def part2(data: str):
    lines = data.splitlines()
    pts = []
    while lines[0]:
        pts.append(tuple(map(int, lines.pop(0).split(","))))
    lines.pop(0)

    nc = max(x[0] for x in pts)
    nr = max(x[1] for x in pts)

    paper = [[0] * (nc + 1) for _ in range(nr + 1)]
    for x, y in pts:
        paper[y][x] = 1

    for instr in lines:
        if "x" in instr:
            col = int(instr[instr.index("=") + 1 :])
            for i in range(len(paper)):
                for j in range(len(paper[i])):
                    if col - j < 0 or col + j >= len(paper[i]):
                        break

                    paper[i][col - j] |= paper[i][col + j]

                paper[i] = paper[i][:col]
        else:
            assert "y" in instr
            row = int(instr[instr.index("=") + 1 :])
            for i in range(len(paper)):
                if row - i < 0 or row + i >= len(paper):
                    break
                paper[row - i] = [x | y for x, y in zip(paper[row - i], paper[row + i])]

            paper = paper[:row]

    for pr in paper:
        print("".join("#" if x else "." for x in pr))


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5""",
# )
