# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 20                   | #
# | 14264 정육각형과 삼각형     | #
# ---------------------------- #


if __name__ == "__main__":
    L = int(r_input())
    print(((3 * 3 ** (1 / 2) * L ** 2) / 2) / 6)
