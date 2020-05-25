# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 15963 CASIO              | #
# ---------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    print(int(N == M))
