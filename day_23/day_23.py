import sys
import os
from icecream import ic
from dataclasses import dataclass
from copy import deepcopy

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run

# cost from each valid hallway to each column (first spot)
hallway_col_cost = {
    0: {0: 3, 1: 5, 2: 7, 3: 9},
    1: {0: 2, 1: 4, 2: 6, 3: 8},
    3: {0: 2, 1: 2, 2: 4, 3: 6},
    5: {0: 4, 1: 2, 2: 2, 3: 4},
    7: {0: 6, 1: 4, 2: 2, 3: 2},
    9: {0: 8, 1: 6, 2: 4, 3: 2},
    10: {0: 9, 1: 7, 2: 5, 3: 3},
}

# map from column to hallway idx right outside (used to check that hallway path is empty)
col_hallway_map = {0: 2, 1: 4, 2: 6, 3: 8}

cost_map = {"A": 1, "B": 10, "C": 100, "D": 1000}
target_col = {"A": 0, "B": 1, "C": 2, "D": 3}


@dataclass(frozen=True)
class Move:
    type: str
    col: int
    col_depth: int
    hallway: int
    col_to_hallway: bool

    def get_cost(self):
        return (self.col_depth + hallway_col_cost[self.hallway][self.col]) * cost_map[
            self.type
        ]


def step(src, to):
    if to < src:
        it = iter(range(src, to - 1, -1))
    else:
        it = iter(range(src, to + 1))
    next(it)
    return it


class Board:
    def __init__(self, cols):
        self.cols = cols
        self.hallways = [""] * 11

        self.memo = {}

    def solve(self):
        # approach: brute force with memoization
        cols_s = "".join("." if not x else x for c in self.cols for x in c)
        hw_s = "".join("." if not x else x for x in self.hallways)
        if (cols_s, hw_s) in self.memo:
            return self.memo[cols_s, hw_s]

        for i in range(len(self.cols)):
            if any(not x or target_col[x] != i for x in self.cols[i]):
                break
        else:
            # all columns are correct
            return 0

        min_cost = float("inf")
        for move in self.get_moves():
            # ic(move)
            # ic(hw_s)
            # ic(cols_s)
            old_cols = deepcopy(self.cols)
            old_hallways = self.hallways.copy()

            if move.col_to_hallway:
                self.hallways[move.hallway] = move.type
                self.cols[move.col][move.col_depth] = ""
            else:
                self.cols[move.col][move.col_depth] = move.type
                self.hallways[move.hallway] = ""

            min_cost = min(min_cost, self.solve() + move.get_cost())

            self.cols = old_cols
            self.hallways = old_hallways

        self.memo[cols_s, hw_s] = min_cost
        return min_cost

    def get_moves(self) -> list[Move]:
        moves = []

        empty_cols = []
        empty_hallways = [i for i in hallway_col_cost.keys() if self.hallways[i] == ""]
        full_hallways = [i for i in hallway_col_cost.keys() if self.hallways[i] != ""]

        movable_cols = []
        for i in range(len(self.cols)):
            # don't move from the column if the column is the target
            # and we aren't blocking anything
            if not all(not x or i == target_col[x] for x in self.cols[i]):
                for j in range(len(self.cols[i])):
                    if self.cols[i][j]:
                        movable_cols.append((i, j))
                        break

            # don't move to the column if we are going to block something
            # from leaving
            for j in range(len(self.cols[i]) - 1, -1, -1):
                if self.cols[i][j] and target_col[self.cols[i][j]] != i:
                    break

                if not self.cols[i][j]:
                    empty_cols.append((i, j))
                    break

        # column to hallway
        for col, col_depth in movable_cols:
            for hallway in empty_hallways:
                if any(
                    self.hallways[x] != "" for x in step(col_hallway_map[col], hallway)
                ):
                    # path is blocked
                    continue

                m = Move(self.cols[col][col_depth], col, col_depth, hallway, True)
                moves.append(m)

        # hallway to column
        for col, col_depth in empty_cols:
            for hallway in full_hallways:
                if any(
                    self.hallways[x] != "" for x in step(hallway, col_hallway_map[col])
                ):
                    # path is blocked
                    continue

                if col_depth == 0:
                    # amphipod that is already in column is not correct
                    if target_col[self.cols[col][1]] != col:
                        continue

                if target_col[self.hallways[hallway]] != col:
                    # incorrect destination
                    continue

                m = Move(self.hallways[hallway], col, col_depth, hallway, False)
                moves.append(m)

        return moves


def part1(data: str):
    cols: list[list[str]] = [[] for _ in range(4)]
    d = data.splitlines()
    for i, a in enumerate(d[2].replace("#", "")):
        cols[i].append(a)
    for i, a in enumerate(d[3].replace("#", "").replace(" ", "")):
        cols[i].append(a)

    b = Board(cols)
    return b.solve()


def part2(data: str):
    cols: list[list[str]] = [[] for _ in range(4)]
    d = data.splitlines()
    for i, a in enumerate(d[2].replace("#", "")):
        cols[i].append(a)
    for i, a in enumerate(d[3].replace("#", "").replace(" ", "")):
        cols[i].append(a)

    n = ["DD", "CB", "BA", "AC"]
    for i in range(4):
        for c in reversed(n[i]):
            cols[i].insert(1, c)

    b = Board(cols)
    return b.solve()


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """""")
