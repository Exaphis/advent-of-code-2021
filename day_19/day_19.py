import sys
import os
from icecream import ic
from collections import defaultdict
from typing import Generator, Optional

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run

P = tuple[int, int, int]  # point
S = tuple[str, int, int]  # state (rotation and direction)


def get_pt(facing: str, d: int, rots: int, pt: P) -> P:
    """
    Get a point's new point given a rotation/facing direction.
    facing: x/y/z
    d: -1 or 1
    rots: number of rotations (0, 1, 2, 3)
    """
    da, db, dc = pt
    if facing == "x":
        main = da
        offa = db
        offb = dc
    elif facing == "y":
        main = db
        offa = dc
        offb = da
    elif facing == "z":
        main = dc
        offa = da
        offb = db

    if d == -1:
        offa, offb = offb, offa

    for _ in range(rots):
        offa, offb = offb, -offa

    return (d * main, offa, offb)


def gen_states() -> Generator[S, None, None]:
    """Find all possible states for a scanner."""
    for facing in "xyz":
        for d in (-1, 1):
            for rots in range(4):
                yield facing, d, rots


def solve_scanner(b1: list[P], b2: list[P]) -> Optional[tuple[S, P]]:
    """Given two lists of beacons, find the state and offset of the 2nd beacon from the 1st beacon."""
    for facing, d, rots in gen_states():
        b2_rot = [get_pt(facing, d, rots, b) for b in b2]
        offsets: defaultdict[P, int] = defaultdict(int)
        for x1, y1, z1 in b1:
            for x2, y2, z2 in b2_rot:
                offsets[(x1 - x2, y1 - y2, z1 - z2)] += 1

        x = list(offsets.keys())
        max_off = max(x, key=lambda x: offsets[x])

        if offsets[max_off] >= 12:
            return (facing, d, rots), max_off

    return None


positions: dict[int, P] = {}


def part1(data: str):
    scanners: list[list[P]] = []
    curr_scanner: list[P] = []
    for line in data.splitlines():
        if line.startswith("---"):
            curr_scanner = []
        elif line:
            x, y, z = tuple(map(int, line.split(",")))
            curr_scanner.append((x, y, z))
        else:
            scanners.append(curr_scanner)

    if curr_scanner:
        scanners.append(curr_scanner)

    # positions of each scanner
    positions[0] = (0, 0, 0)

    # list of all beacons (normalized to position and state of scanner 0)
    pts: defaultdict[P, int] = defaultdict(int)
    for pt in scanners[0]:
        pts[pt] += 1

    known = {0}
    unknown = set(range(len(scanners))) - {0}
    while unknown:
        found = False
        for i in known:
            for j in unknown:
                ans = solve_scanner(scanners[i], scanners[j])
                if ans is not None:
                    found = True
                    (facing, d, rots), off = ans

                    positions[j] = off

                    # update points to normalize to scanner 0's rotation and position
                    new_pts = []
                    for x, y, z in scanners[j]:
                        x, y, z = get_pt(facing, d, rots, (x, y, z))
                        x += off[0]
                        y += off[1]
                        z += off[2]
                        new_pts.append((x, y, z))
                        pts[x, y, z] += 1
                    scanners[j] = new_pts

                    dup = set(scanners[i]) & set(scanners[j])
                    break

            if found:
                break

        assert found
        ic("learned", j, "from", i)
        ic("missing", len(unknown))

        known.add(j)
        unknown.remove(j)

    return len(pts)


def part2(data: str):
    max_dist = 0
    p = list(positions.values())
    for i in range(1, len(p)):
        for j in range(i):
            dist = 0
            for z in range(3):
                dist += abs(p[i][z] - p[j][z])

            max_dist = max(max_dist, dist)

    return max_dist


run(part1, part2, os.path.join(local_dir, "input.txt"))
