import sys
import os
from icecream import ic
from collections import defaultdict

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    def rec(neighbors, curr, visited=set()):
        if curr == "end":
            return 1

        paths = 0
        for n in neighbors[curr]:
            if n == n.lower() and n in visited:
                continue
            paths += rec(neighbors, n, visited | {n})

        return paths

    neighbors = defaultdict(list)
    for line in data.splitlines():
        a, b = line.split("-")
        neighbors[a].append(b)
        neighbors[b].append(a)

    return rec(neighbors, "start", {"start"})


def part2(data: str):
    def rec(neighbors, curr, visited):
        if curr == "end":
            return 1

        paths = 0
        for n in neighbors[curr]:
            q = visited.copy()

            if n == n.lower():
                twice = any(c == 2 for k, c in visited.items() if k != "start")

                if twice and visited[n] >= 1:
                    continue
                elif not twice and visited[n] >= 2:
                    continue

                q[n] += 1

            paths += rec(neighbors, n, q)

        return paths

    neighbors = defaultdict(list)
    for line in data.splitlines():
        a, b = line.split("-")
        neighbors[a].append(b)
        neighbors[b].append(a)

    v = defaultdict(int)
    v["start"] = 2
    return rec(neighbors, "start", v)


run(part1, part2, os.path.join(local_dir, "input.txt"))
