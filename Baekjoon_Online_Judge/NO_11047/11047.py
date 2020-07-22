# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 22                   | #
# | 11047 동전 0              | #
# ---------------------------- #


if __name__ == "__main__":
    N, K = map(int, r_input().split())

    coins = [int(r_input()) for _ in range(N)]
    res = 0

    for ind in range(N - 1, -1, -1):
        res += K // coins[ind]

        K %= coins[ind]
    
    print(res)
