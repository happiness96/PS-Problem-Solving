# -*- encoding: utf-8 -*-
import sys
from itertools import permutations
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 15649 N과 M (1)           | #
# ---------------------------- #


def run():
    N, M = map(int, r_input().split())

    for case in permutations(range(1, N + 1), M):
        print(*case)


if __name__ == "__main__":
    run()
