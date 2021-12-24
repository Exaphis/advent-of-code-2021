import sys
import os
from icecream import ic
import z3
from copy import copy

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run

# see test.py for notes


def gen_solver(data: str, digits):
    d = data.split("inp w")
    blocks = []
    for block in d:
        if not block:
            continue

        lines = [x for x in block.splitlines() if x]
        assert len(lines) == 17

        shift_z = lines[3] == "div z 26"
        x_inc = int(lines[4].split()[-1])
        y_inc = int(lines[-3].split()[-1])

        assert y_inc <= 16

        blocks.append((shift_z, x_inc, y_inc))

    s = z3.Solver()
    for d in digits:
        s.add(d > 0, d <= 9)  # type: ignore

    stack = []  # type: ignore
    for i, (shift_z, x_inc, y_inc) in enumerate(blocks):
        if not stack:
            x = 0
        else:
            x = stack[-1]

        if shift_z:
            stack.pop()

        if x_inc < 10:
            s.add(x + x_inc == digits[i])
        else:
            stack.append(digits[i] + y_inc)

    return s


def part1(data: str):
    digits = [z3.Int(f"d{i}") for i in range(14)]
    s = gen_solver(data, digits)

    answer = [0] * 14
    for i in range(14):
        for test_digit in range(9, 0, -1):
            answer[i] = test_digit

            solver = copy(s)

            for j in range(i + 1):
                solver.add(digits[j] == answer[j])

            if solver.check() == z3.sat:
                break
        else:
            return None

    return "".join(map(str, answer))


def part2(data: str):
    digits = [z3.Int(f"d{i}") for i in range(14)]
    s = gen_solver(data, digits)

    answer = [0] * 14
    for i in range(14):
        for test_digit in range(1, 10):
            answer[i] = test_digit

            solver = copy(s)

            for j in range(i + 1):
                solver.add(digits[j] == answer[j])

            if solver.check() == z3.sat:
                break
        else:
            return None

    return "".join(map(str, answer))


run(part1, part2, os.path.join(local_dir, "input.txt"))
