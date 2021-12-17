import sys
import os
from icecream import ic

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


def part1(data: str):
    x_min, x_max = map(int, data[data.find("x=") + 2 : data.find(",")].split(".."))
    y_min, y_max = map(int, data[data.find("y=") + 2 :].split(".."))

    for ny_vel in range(500, -250, -1):
        for nx_vel in range(1, x_max + 1):
            x_vel = nx_vel
            y_vel = ny_vel

            x = 0
            y = 0
            max_y = 0

            while True:
                x += x_vel
                y += y_vel

                max_y = max(max_y, y)
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1

                if x_min <= x <= x_max and y_min <= y <= y_max:
                    return max_y

                if x > x_max or y < y_min:
                    break

    return None


def part2(data: str):
    x_min, x_max = map(int, data[data.find("x=") + 2 : data.find(",")].split(".."))
    y_min, y_max = map(int, data[data.find("y=") + 2 :].split(".."))

    vels = set()
    for ny_vel in range(500, -500, -1):
        for nx_vel in range(1, x_max + 1):
            x_vel = nx_vel
            y_vel = ny_vel

            x = 0
            y = 0
            max_y = 0

            while True:
                x += x_vel
                y += y_vel

                max_y = max(max_y, y)
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1

                if x_min <= x <= x_max and y_min <= y <= y_max:
                    vels.add((nx_vel, ny_vel))
                    break

                if x > x_max or y < y_min:
                    break

    return len(vels)


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(part1, part2, """target area: x=20..30, y=-10..-5""")
