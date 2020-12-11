# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 11                             | #
# | 2869 달팽이는 올라가고 싶다         | #
# -------------------------------------- #


if __name__ == "__main__":
    A, B, V = map(int, r_input().split())

    per_day = A - B
    V -= A

    print(V // per_day + int(V % per_day != 0) + 1)
