# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | A + B - 4                          | #
# -------------------------------------- #


if __name__ == "__main__":
    for numbers in sys.stdin:
        A, B = map(int, numbers.split())
        print(A + B)
