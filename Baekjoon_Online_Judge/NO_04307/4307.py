# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 4307 개미                 | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        stick_len, n = map(int, r_input().split())

        ants_loc = [int(r_input()) for _ in range(n)]

        mini = 0
        maxi = 0

        for loc in ants_loc:
            mini = max(mini, min(loc, stick_len - loc))
            maxi = max(maxi, max(loc, stick_len - loc))
        
        print(mini, maxi)


if __name__ == "__main__":
    run()
