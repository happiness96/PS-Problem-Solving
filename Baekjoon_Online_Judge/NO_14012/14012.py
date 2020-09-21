# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 22                             | #
# | 14012 Large PhD Restaurant         | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    A = list(map(int, r_input().split()))
    B = list(map(int, r_input().split()))

    cost = []

    for ind in range(N):
        cost.append((A[ind], B[ind]))
    
    cost.sort()

    for a, b in cost:
        gap = b - a

        if gap > 0 and a <= M:
            M += gap
    
    print(M)


if __name__ == "__main__":
    run()
