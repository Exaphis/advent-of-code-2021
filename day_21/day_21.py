import sys
import os
from typing import Generator
from icecream import ic
from collections import defaultdict
from itertools import product

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def gen_rolls() -> Generator[int, None, None]:
    i = 1
    while True:
        yield i
        i += 1
        if i == 101:
            i = 1


def update_player(roll_sum: int, pos: int, score: int) -> tuple[int, int]:
    pos = (pos + roll_sum) % 10
    score += 10 if pos == 0 else pos

    return pos, score


def part1(data: str):
    l = data.splitlines()
    p1 = int(l[0].split(": ")[-1])
    p2 = int(l[1].split(": ")[-1])

    p1s = 0
    p2s = 0

    g = gen_rolls()
    rolls = 0
    p1p = True
    while p1s < 1000 and p2s < 1000:
        roll_sum = sum(next(g) for _ in range(3))
        rolls += 3
        if p1p:
            p1, p1s = update_player(roll_sum, p1, p1s)
        else:
            p2, p2s = update_player(roll_sum, p2, p2s)

        p1p = not p1p

    return rolls * min(p1s, p2s)


def part2(data: str):
    l = data.splitlines()
    p1start = int(l[0].split(": ")[-1])
    p2start = int(l[1].split(": ")[-1])

    # state type
    # (player1 pos, player2 pos, player1 score, player2 score)
    S = tuple[int, int, int, int]
    scores: defaultdict[S, int] = defaultdict(int)
    scores[p1start, p2start, 0, 0] += 1

    p1_wins = 0
    p2_wins = 0

    op1p = True
    while scores:
        new_scores: defaultdict[S, int] = defaultdict(int)
        for (op1, op2, op1s, op2s), freq in scores.items():
            for d1, d2, d3 in product([1, 2, 3], repeat=3):
                p1, p2, p1s, p2s, p1p = op1, op2, op1s, op2s, op1p
                roll_sum = d1 + d2 + d3
                if p1p:
                    p1, p1s = update_player(roll_sum, p1, p1s)
                else:
                    p2, p2s = update_player(roll_sum, p2, p2s)

                if p1s >= 21:
                    p1_wins += freq
                elif p2s >= 21:
                    p2_wins += freq
                else:
                    new_scores[p1, p2, p1s, p2s] += freq

        scores = new_scores
        op1p = not op1p

    return max(p1_wins, p2_wins)


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """""")
