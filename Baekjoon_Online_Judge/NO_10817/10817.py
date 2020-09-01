# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 01                             | #
# | 세 수                              | #
# -------------------------------------- #


if __name__ == "__main__":
    numbers = list(map(int, r_input().split()))

    print(sorted(numbers)[1])
