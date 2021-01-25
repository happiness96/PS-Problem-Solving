# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 25                             | #
# | 13699 점화식                       | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    t = [0] * (n + 1)

    t[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            t[i] += t[j] * t[i - j - 1]

    print(t[n])
