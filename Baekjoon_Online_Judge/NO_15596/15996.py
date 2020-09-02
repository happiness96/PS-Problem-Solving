# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 정수 N개의 합                       | #
# -------------------------------------- #


def solve(a: list) -> int:
    ans = 0

    for val in a:
        ans += val

    return ans
