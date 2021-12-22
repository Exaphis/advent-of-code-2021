import sys
import os
from typing import Generator
from icecream import ic
from collections import defaultdict
from dataclasses import dataclass
from copy import copy

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


@dataclass
class Prism:
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int

    def volume(self):
        return self.dx * self.dy * self.dz

    def difference(self, other):
        if not self.overlap(other):
            return [self]

        return list(prism_difference(self, other))

    def overlap(self, other):
        overlap_x = (self.x + self.dx > other.x) and (self.x < other.x + other.dx)
        overlap_y = (self.y + self.dy > other.y) and (self.y < other.y + other.dy)
        overlap_z = (self.z + self.dz > other.z) and (self.z < other.z + other.dz)
        return overlap_x and overlap_y and overlap_z


def prism_difference(p1c: Prism, p2c: Prism):
    p1 = copy(p1c)
    p2 = copy(p2c)

    bottom = Prism(p1.x, p1.y, p1.z, p1.dx, p1.dy, p2.z - p1.z)
    top = Prism(p1.x, p1.y, p2.z + p2.dz, p1.dx, p1.dy, (p1.z + p1.dz) - (p2.z + p2.dz))

    new_max_z = min(p1.z + p1.dz, p2.z + p2.dz)
    p1.z = max(p1.z, p2.z)
    p1.dz = new_max_z - p1.z

    s1 = Prism(p1.x, p1.y, p1.z, p1.dx, p2.y - p1.y, p1.dz)
    s2 = Prism(p1.x, p2.y + p2.dy, p1.z, p1.dx, (p1.y + p1.dy) - (p2.y + p2.dy), p1.dz)

    new_max_y = min(p1.y + p1.dy, p2.y + p2.dy)
    p1.y = max(p1.y, p2.y)
    p1.dy = new_max_y - p1.y

    s3 = Prism(p1.x, p1.y, p1.z, p2.x - p1.x, p1.dy, p1.dz)
    s4 = Prism(p2.x + p2.dx, p1.y, p1.z, (p1.x + p1.dx) - (p2.x + p2.dx), p1.dy, p1.dz)

    outs = [top, bottom, s1, s2, s3, s4]
    for p in outs:
        if p.dx > 0 and p.dy > 0 and p.dz > 0:
            yield p


def part1(data: str):
    cubes = [[[False] * 100 for _ in range(100)] for _ in range(100)]
    for line in data.splitlines():
        state, pos = line.split(" ")
        xs, ys, zs = pos.split(",")
        xs = xs[2:]
        ys = ys[2:]
        zs = zs[2:]
        x_min, x_max = map(int, xs.split(".."))
        y_min, y_max = map(int, ys.split(".."))
        z_min, z_max = map(int, zs.split(".."))

        x_min = max(x_min, -50)
        y_min = max(y_min, -50)
        z_min = max(z_min, -50)
        x_max = min(x_max, 50)
        y_max = min(y_max, 50)
        z_max = min(z_max, 50)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    cubes[x + 50][y + 50][z + 50] = state == "on"
    cnt = 0
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if cubes[x][y][z]:
                    cnt += 1
    return cnt


def part2(data: str):
    prisms: list[Prism] = []
    for i, line in enumerate(data.splitlines()):
        ic(i)
        state, pos = line.split(" ")
        xs, ys, zs = pos.split(",")
        xs = xs[2:]
        ys = ys[2:]
        zs = zs[2:]

        x_min, x_max = map(int, xs.split(".."))
        y_min, y_max = map(int, ys.split(".."))
        z_min, z_max = map(int, zs.split(".."))
        x_max += 1
        y_max += 1
        z_max += 1

        p = Prism(x_min, y_min, z_min, x_max - x_min, y_max - y_min, z_max - z_min)
        if state == "on":
            to_add = [p]

            # remove existing prisms from new prism
            for p2 in prisms:
                new_to_add: list[Prism] = []
                for p1 in to_add:
                    new_to_add.extend(p1.difference(p2))

                to_add = new_to_add

            prisms.extend(to_add)
        else:
            new_prisms: list[Prism] = []
            for p1 in prisms:
                new_prisms.extend(p1.difference(p))

            prisms = new_prisms

        # prisms list should be disjoint

    cnt = 0
    for p in prisms:
        cnt += p.volume()

    return cnt


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """on x=10..12,y=10..12,z=10..12
# on x=11..13,y=11..13,z=11..13
# off x=9..11,y=9..11,z=9..11
# on x=10..10,y=10..10,z=10..10""",
# )
# ic(Prism(1, 1, 1, 2, 2, 2).difference(Prism(0, 0, 0, 2, 2, 2)))
