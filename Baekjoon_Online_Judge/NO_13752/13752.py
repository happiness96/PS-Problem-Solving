# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 13752 히스토그램           | #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    for _ in range(n):
        k = int(r_input())

        print('=' * k)
