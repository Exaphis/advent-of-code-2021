import sys
import os
from icecream import ic
from math import ceil
from dataclasses import dataclass
from typing import Optional, cast

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))
from aoc import run


@dataclass
class Node:
    val: Optional[int] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def is_number(self):
        return self.val is not None

    def is_pair(self):
        return self.left is not None and self.right is not None


def simplify_nums(root: Node) -> bool:
    visit = [root]
    while visit:
        curr = visit.pop()
        if curr.is_number():
            val = cast(int, curr.val)
            if val >= 10:
                curr.val = None
                curr.left = Node(val // 2)
                curr.right = Node(ceil(val / 2))
                return True
        elif curr.is_pair():
            visit.append(cast(Node, curr.right))
            visit.append(cast(Node, curr.left))
        else:
            assert False

    return False


def simplify_pairs(root: Node) -> bool:
    visit = [(0, root)]
    prev_num: Optional[Node] = None
    to_add: Optional[int] = None

    while visit:
        depth, curr = visit.pop()

        if to_add is None:
            if depth == 4 and curr.is_pair():
                curr.left = cast(Node, curr.left)
                curr.right = cast(Node, curr.right)
                assert curr.left.val is not None
                assert curr.right.val is not None

                if prev_num is not None:
                    assert prev_num.val is not None
                    prev_num.val += curr.left.val

                to_add = curr.right.val

                curr.val = 0
                curr.left = None
                curr.right = None

            elif curr.is_number():
                prev_num = curr
        else:
            if curr.val is not None:
                curr.val += to_add
                return True

        if curr.is_pair():
            visit.append((depth + 1, cast(Node, curr.right)))
            visit.append((depth + 1, cast(Node, curr.left)))

    if to_add is not None:
        return True

    return False


def reduce(root: Node):
    while True:
        if not simplify_pairs(root):
            if not simplify_nums(root):
                break


def to_tree(l) -> Node:
    if isinstance(l, int):
        return Node(l)
    else:
        left = to_tree(l[0])
        right = to_tree(l[1])
        return Node(left=left, right=right)


def mag(t: Node) -> int:
    if t.left is not None and t.right is not None:
        return 3 * mag(t.left) + 2 * mag(t.right)
    elif t.val is not None:
        return t.val

    assert False


def part1(data: str):
    c: Optional[Node] = None
    for line in data.splitlines():
        t = to_tree(eval(line))
        if c is None:
            c = t
        else:
            c = Node(left=c, right=t)

        reduce(c)

    if c is not None:
        return mag(c)


def part2(data: str):
    best = 0
    for line1 in data.splitlines():
        for line2 in data.splitlines():
            t1 = to_tree(eval(line1))
            t2 = to_tree(eval(line2))
            c = Node(left=t1, right=t2)
            reduce(c)
            best = max(best, mag(c))

    return best


run(part1, part2, os.path.join(local_dir, "input.txt"))
# run(
#     part1,
#     part2,
#     """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""",
# )
