# -*- encoding: utf-8 -*-
import sys
from math import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 07                             | #
# | 16935 파스칼의 삼각형               | #
# -------------------------------------- #


if __name__ == "__main__":
    n, k = map(int, r_input().split())

    n -= 1
    k -= 1

    print(int(factorial(n)) // (int(factorial(k)) * int(factorial(n - k))))
