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
        signals_s, output = line.split(" | ")
        signals = signals_s.split()
        wire_map = {}
        num_map = {}

        for wires in signals:
            if len(wires) == 2:
                wire_map[wires] = 1
                num_map[1] = wires
            elif len(wires) == 3:
                wire_map[wires] = 7
                num_map[7] = wires
            elif len(wires) == 4:
                wire_map[wires] = 4
                num_map[4] = wires
            elif len(wires) == 7:
                wire_map[wires] = 8
                num_map[8] = wires

        for wires in signals:
            if wires in wire_map:
                continue
            c = set(wires)

            if len(c & set(num_map[1])) == 1:
                # 2, 5, or 6
                if len(c & set(num_map[4])) == 2:
                    wire_map[wires] = 2
                    num_map[2] = wires
                else:
                    # 5 or 6
                    if len(c) == 5:
                        wire_map[wires] = 5
                        num_map[5] = wires
                    else:
                        assert len(c) == 6
                        wire_map[wires] = 6
                        num_map[6] = wires
            else:
                # 0, 3, or 9
                if len(c) == 5:
                    wire_map[wires] = 3
                    num_map[3] = wires
                else:
                    if len(c & set(num_map[4])) == 4:
                        wire_map[wires] = 9
                        num_map[9] = wires
                    else:
                        wire_map[wires] = 0
                        num_map[0] = wires

        # ic(wire_map)
        # ic(num_map)

        m_map = {frozenset(wires): wire_map[wires] for wires in wire_map}
        num = ""
        for wires in output.split():
            num += str(m_map[frozenset(wires)])
        ic(num)
        ret += int(num)
    return ret


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """""")
