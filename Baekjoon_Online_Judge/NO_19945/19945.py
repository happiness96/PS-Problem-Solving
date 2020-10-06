# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19945 새로운 언어 CC               | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    print(len(bin(n)) - 2 if n >= 0 else 32)