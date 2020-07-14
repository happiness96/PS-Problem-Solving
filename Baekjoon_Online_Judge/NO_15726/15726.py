# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 13                   | #
# | 15726 이칙연산            | #
# ---------------------------- #


if __name__ == "__main__":
    A, B, C = map(int, r_input().split())

    print(int(max(A * B / C, A / B * C)))
