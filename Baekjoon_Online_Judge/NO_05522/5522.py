# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 19                   | #
# | 5522 카드 게임            | #
# ---------------------------- #


if __name__ == "__main__":
    print(sum([int(r_input()) for _ in range(5)]))
