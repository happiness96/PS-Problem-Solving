# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 11055 가장 큰 증가 부분 수열        | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    A = list(map(int, r_input().split()))

    dp = [0] * 1001

    for val in A:
        dp[val] = max(dp[val], max(dp[: val]) + val)
    
    print(max(dp))
