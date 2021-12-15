import sys
import os
from icecream import ic
import heapq

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    m = []
    for line in data.splitlines():
        m.append(list(map(int, line)))

    seen = set()
    visit = [(0, (0, 0))]
    while visit:
        visit.sort()
        risk, (r, c) = visit.pop(0)

        if (r, c) in seen:
            continue

        seen.add((r, c))
        if r == len(m) - 1 and c == len(m[r]) - 1:
            return risk

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= r + dr < len(m) and 0 <= c + dc < len(m[r]):
                visit.append((risk + m[r + dr][c + dc], (r + dr, c + dc)))

    return None


def part2(data: str):
    q = []
    for line in data.splitlines():
        q.append(list(map(int, line)))

    m = [[0] * len(q[0] * 5) for _ in range(len(q) * 5)]
    for mr in range(5):
        for mc in range(5):
            diff = mr + mc
            for r in range(len(q)):
                for c in range(len(q[r])):
                    val = q[r][c]

                    for _ in range(diff):
                        val += 1
                        if val > 9:
                            val = 1

                    m[mr * len(q) + r][mc * len(q[0]) + c] = val

    seen = set()
    visit = [(0, (0, 0))]
    while visit:
        risk, (r, c) = heapq.heappop(visit)

        if (r, c) in seen:
            continue

        seen.add((r, c))
        if r == len(m) - 1 and c == len(m[r]) - 1:
            return risk

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= r + dr < len(m) and 0 <= c + dc < len(m[r]):
                new = (risk + m[r + dr][c + dc], (r + dr, c + dc))
                heapq.heappush(visit, new)

    return None


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""",
# )
