import sys
import os
from icecream import ic
from typing import Tuple

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


# def parse_packet(bits: list[int]) -> list[int]:
#     version = int("".join(map(str, bits[:3])), 2)
#     bits = bits[3:]
#     type_id = int("".join(map(str, bits[:3])), 2)
#     bits = bits[3:]

#     return data

s = 0


def part1(data: str):
    line = "".join(bin(int(x, 16))[2:].zfill(4) for x in data)
    bits = list(line)
    get_packet(bits)
    return s


def get_packet(bits: list[str]) -> Tuple[int, list[str]]:
    global s
    if all(x == "0" for x in bits):
        assert False
        return 0, []

    version = int("".join(bits[:3]), 2)
    s += version
    bits = bits[3:]
    type_id = int("".join(bits[:3]), 2)
    bits = bits[3:]

    if type_id == 4:
        num_s = ""

        end = False
        while not end:
            part = bits[:5]
            end = part.pop(0) == "0"
            bits = bits[5:]
            num_s += "".join(part)

        num = int(num_s, 2)
        return num, bits

    length_type_id = int(bits[0])
    bits = bits[1:]

    vals = []
    if length_type_id == 0:
        sub_len = int("".join(bits[:15]), 2)
        bits = bits[15:]

        curr_len = len(bits)
        while curr_len - len(bits) < sub_len:
            val, bits = get_packet(bits)
            vals.append(val)
        assert curr_len - len(bits) == sub_len
    else:
        num_subpackets = int("".join(bits[:11]), 2)
        bits = bits[11:]

        for _ in range(num_subpackets):
            val, bits = get_packet(bits)
            vals.append(val)

    if type_id == 0:
        return sum(vals), bits
    elif type_id == 1:
        o = 1
        for v in vals:
            o *= v
        return o, bits
    elif type_id == 2:
        return min(vals), bits
    elif type_id == 3:
        return max(vals), bits
    elif type_id == 5:
        assert len(vals) == 2
        return int(vals[0] > vals[1]), bits
    elif type_id == 6:
        assert len(vals) == 2
        return int(vals[0] < vals[1]), bits
    elif type_id == 7:
        assert len(vals) == 2
        return int(vals[0] == vals[1]), bits
    else:
        assert False
        return 0, []


def part2(data: str):
    line = "".join(bin(int(x, 16))[2:].zfill(4) for x in data)
    bits = list(line)

    return get_packet(bits)[0]


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """D2FE28""")
