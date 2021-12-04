import sys
import os
from icecream import ic
from collections import Counter

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def get_freqs(bits, idx):
    c = Counter(bit[idx] for bit in bits)
    return c["1"], c["0"]


def part1(data: str):
    bits = data.splitlines()
    l = len(bits[0])

    gamma = ""
    eps = ""
    for i in range(l):
        freq_1 = 0
        for j in range(len(bits)):
            if bits[j][i] == "1":
                freq_1 += 1

        if freq_1 > (len(bits) - freq_1):
            gamma += "1"
            eps += "0"
        else:
            gamma += "0"
            eps += "1"

    ic(gamma, eps)
    return int(gamma, 2) * int(eps, 2)


def part2(data: str):
    bits = data.splitlines()
    l = len(bits[0])
    oxy = bits.copy()
    co2 = bits.copy()

    for i in range(l):
        os, zs = get_freqs(oxy, i)
        most = "1" if os >= zs else "0"

        os, zs = get_freqs(co2, i)
        least = "0" if os >= zs else "1"

        # ic(most, least)
        if len(oxy) > 1:
            oxy = [bit for bit in oxy if bit[i] == most]

        if len(co2) > 1:
            co2 = [bit for bit in co2 if bit[i] == least]

        # ic(oxy)
        # ic(co2)

    assert len(oxy) == 1 and len(co2) == 1
    ox = int(list(oxy)[0], 2)
    co = int(list(co2)[0], 2)
    ic(ox, co)
    return ox * co


run(part1, part2, os.path.join(local_dir, "input.txt"))
