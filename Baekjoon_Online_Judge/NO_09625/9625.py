# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 18                             | #
# | 9625 BABBA                         | #
# -------------------------------------- #


if __name__ == "__main__":
    K = int(r_input())

    AB = [1, 0]

    for _ in range(K):
        AB[0], AB[1] = AB[1], AB[0] + AB[1]

    print(*AB)
