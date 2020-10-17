# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 17                             | #
# | 9237 이장님 초대                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    t = list(map(int, r_input().split()))
    t.sort(reverse=True)

    res = 0

    for ind, val in enumerate(t):
        res = max(res, ind + val)
    
    print(res + 2)


if __name__ == "__main__":
    run()
