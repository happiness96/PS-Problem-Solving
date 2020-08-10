# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 10                             | #
# | 19532 수학은 비대면강의입니다         | #
# -------------------------------------- #


if __name__ == "__main__":
    a, b, c, d, e, f = map(int, r_input().split())

    x = (c * e - f * b) // (a * e - d * b)
    y = (c * d - f * a) // (b * d - a * e)

    print(x, y)
