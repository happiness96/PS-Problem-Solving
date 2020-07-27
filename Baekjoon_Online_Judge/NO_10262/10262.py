# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 27                   | #
# | 10262 주사위 게임          | #
# ---------------------------- #


if __name__ == "__main__":
    a1, b1, a2, b2 = map(int, r_input().split())
    a3, b3, a4, b4 = map(int, r_input().split())

    a1 += a2 + b1 + b2
    a3 += a4 + b3 + b4

    print('Emma' if a3 > a1 else 'Gunnar' if a3 < a1 else 'Tie')
