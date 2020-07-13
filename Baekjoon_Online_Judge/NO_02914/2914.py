# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 13                   | #
# | 2914 저작권               | #
# ---------------------------- #


if __name__ == "__main__":
    A, I = map(int, r_input().split())
    print(A * (I - 1) + 1)
