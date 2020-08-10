# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 10                             | #
# | 18883 N M 찍기                     | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    for i in range(N):
        print(' '.join([str(M * i + j) for j in range(1, M + 1)]))


if __name__ == "__main__":
    run()
