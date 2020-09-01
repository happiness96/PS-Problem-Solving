# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 01                             | #
# | 구구단                             | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    for i in range(1, 10):
        print(N, '*', i, '=', N * i)
