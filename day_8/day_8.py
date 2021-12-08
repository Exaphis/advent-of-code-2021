import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    count = 0
    for line in data.splitlines():
        _, output = line.split(" | ")
        for n in output.split():
            if len(n) in (2, 4, 3, 7):
                count += 1

    return count


def part2(data: str):
    ret = 0

    for line in data.splitlines():
        wires_list_s, output = line.split(" | ")
        wires_list = ["".join(sorted(wires)) for wires in wires_list_s.split()]
        wires_map = [""] * 10

        # find known numbers using the number of wires
        len_num_map = {2: 1, 3: 7, 4: 4, 7: 8}
        for wires in wires_list:
            if len(wires) in len_num_map:
                wires_map[len_num_map[len(wires)]] = wires

        # find all unknown numbers by checking which wires are in common with known
        # wires as well as using its number of wires
        for wires in wires_list:
            if wires in wires_map:
                continue

            c = set(wires)

            if len(c & set(wires_map[1])) == 1:
                # 2, 5, or 6
                if len(c & set(wires_map[4])) == 2:
                    wires_map[2] = wires
                else:
                    # 5 or 6
                    if len(c) == 5:
                        wires_map[5] = wires
                    else:
                        assert len(c) == 6
                        wires_map[6] = wires
            else:
                # 0, 3, or 9
                if len(c) == 5:
                    wires_map[3] = wires
                else:
                    if len(c & set(wires_map[4])) == 4:
                        wires_map[9] = wires
                    else:
                        wires_map[0] = wires

        assert not any(not wire for wire in wires_map)

        num = ""
        for wires in output.split():
            wires = "".join(sorted(wires))
            num += str(wires_map.index(wires))
        # ic(num)
        ret += int(num)
    return ret


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """""")
