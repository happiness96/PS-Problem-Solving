# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 10                             | #
# | 17496 스타후르츠                    | #
# -------------------------------------- #


if __name__ == "__main__":
    N, T, C, P = map(int, r_input().split())

    print((N- 1) // T * C * P)
