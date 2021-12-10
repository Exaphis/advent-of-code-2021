import sys
import os
from icecream import ic
from statistics import median

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    m = {"{": "}", "[": "]", "(": ")", "<": ">"}
    out = 0
    for line in data.splitlines():
        stack = []
        for char in line:
            if char in m:
                stack.append(m[char])
            else:
                if stack[-1] != char:
                    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
                    out += points[char]
                    # ic(char, out)
                    break
                stack.pop()
    return out


def part2(data: str):
    m = {"{": "}", "[": "]", "(": ")", "<": ">"}

    scores = []
    for line in data.splitlines():
        stack = []
        for char in line:
            if char in m:
                stack.append(m[char])
            else:
                if stack[-1] != char:
                    break
                stack.pop()
        else:
            score = 0
            for c in reversed(stack):
                score *= 5
                points = {")": 1, "]": 2, "}": 3, ">": 4}
                score += points[c]

            scores.append(score)

    return median(scores)


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """[({(<(())[]>[[{[]{<()<>>""")
