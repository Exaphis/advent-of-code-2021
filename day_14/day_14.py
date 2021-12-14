import sys
import os
from icecream import ic
from collections import Counter, defaultdict

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(datas: str):
    data = datas.splitlines()
    template = data.pop(0)
    data.pop(0)

    maps = {}
    for rule in data:
        k, v = rule.split(" -> ")
        maps[k] = v

    for _ in range(10):
        nt = template[0]
        for i in range(1, len(template)):
            pair = template[i - 1] + template[i]
            if pair in maps:
                nt += maps[pair]
            nt += template[i]

        template = nt
        # ic(template)

    c = Counter(template)
    return max(c.values()) - min(c.values())


def part2(datas: str):
    data = datas.splitlines()
    template = data.pop(0)
    data.pop(0)

    maps = {}
    for rule in data:
        k, v = rule.split(" -> ")
        maps[k] = v

    pairs: defaultdict[str, int] = defaultdict(int)
    for i in range(1, len(template)):
        pair = template[i - 1] + template[i]
        pairs[pair] += 1

    c = Counter(template)

    for _ in range(40):
        np: defaultdict[str, int] = defaultdict(int)

        for pair, freq in pairs.items():
            if pair in maps:
                a, b = pair[0], pair[1]
                np[a + maps[pair]] += freq
                c[maps[pair]] += freq
                np[maps[pair] + b] += freq
            else:
                np[pair] += freq

        pairs = np
        ic(pairs)

    return max(c.values()) - min(c.values())


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""",
# )
