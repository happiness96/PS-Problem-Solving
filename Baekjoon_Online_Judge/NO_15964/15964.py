# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 07                   | #
# | 15964 이상한 기호         | #
# ---------------------------- #


if __name__ == "__main__":
    A, B = map(int, r_input().split())

    print((A + B) * (A - B))
