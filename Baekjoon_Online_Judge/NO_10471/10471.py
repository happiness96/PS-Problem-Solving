# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 22                             | #
# | 10471 공간을 만들어 봅시다.          | #
# -------------------------------------- #


def run():
    W, P = map(int, r_input().split())

    L = list(map(int, r_input().split())) + [W]

    res = set()

    for ind1, val in enumerate(L):
        res.add(val)

        for ind2 in range(ind1):
            res.add(val - L[ind2])
    
    print(*sorted(res))


if __name__ == "__main__":
    run()
