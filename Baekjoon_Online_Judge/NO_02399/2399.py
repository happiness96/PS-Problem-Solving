# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 27                             | #
# | 2399 거리의 합                       | #
# -------------------------------------- #


def run():
    n = int(r_input())

    res = 0
    locs = sorted(map(int, r_input().split()))
    tot = sum(locs)
    
    for ind, loc in enumerate(locs):
        res += tot - loc * (n - ind)
        tot -= loc

    print(res * 2)


if __name__ == "__main__":
    run()
