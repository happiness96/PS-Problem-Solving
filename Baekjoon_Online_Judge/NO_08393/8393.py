# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 8393 합                  | #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    print(n * (1 + n) // 2)
