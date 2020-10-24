# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 24                             | #
# | 1459 걷기                          | #
# -------------------------------------- #


if __name__ == "__main__":
    X, Y, W, S = map(int, r_input().split())

    res1 = (X + Y) * W
    res2 = (max(X, Y) - (max(X, Y) - min(X, Y)) % 2) * S + (max(X, Y) - min(X, Y)) % 2 * W
    res3 = min(X, Y) * S + (max(X, Y) - min(X, Y)) * W

    print(min(res1, res2, res3))
