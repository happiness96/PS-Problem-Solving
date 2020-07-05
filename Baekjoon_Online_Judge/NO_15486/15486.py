# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 05                   | #
# | 15486 퇴사 2              | #
# ---------------------------- #


def run():
    N = int(r_input())

    dp = [0] * (N + 1)

    maxi = 0

    for i in range(N):
        T, P = map(int, r_input().split())

        maxi = max(maxi, dp[i])
        aft_ind = i + T

        if aft_ind <= N:
            dp[aft_ind] = max(dp[aft_ind], maxi + P)
    
    print(max(maxi, dp[-1]))


if __name__ == "__main__":
    run()
