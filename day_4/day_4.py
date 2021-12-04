import sys
import os
from typing import Tuple
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def is_win(board: list[list[int]]) -> bool:
    for row in board:
        if sum(row) == -5:
            return True
    for i in range(len(board[0])):
        if sum(row[i] for row in board) == -5:
            return True
    return False


def parse_input(data: str) -> Tuple[list[int], list[list[list[int]]]]:
    lines = data.splitlines()
    nums = list(map(int, lines.pop(0).split(",")))

    boards = []
    while lines:
        lines.pop(0)
        board = []
        for _ in range(5):
            board.append(list(map(int, lines.pop(0).split())))
        boards.append(board)

    return nums, boards


def part1(data: str):
    nums, boards = parse_input(data)

    for num in nums:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1

            if is_win(board):
                return sum(n for row in board for n in row if n != -1) * num
    ic(boards)
    return None


def part2(data: str):
    nums, boards = parse_input(data)

    last_won = (-1, -1)
    won = set()
    for num in nums:
        for it, board in enumerate(boards):
            if it in won:
                continue

            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1

            if is_win(board):
                last_won = (it, num)
                won.add(it)

    ic(last_won)
    assert last_won != -1
    i, num = last_won
    return sum(n for row in boards[i] for n in row if n != -1) * num


run(part1, part2, os.path.join(local_dir, "input.txt"))
