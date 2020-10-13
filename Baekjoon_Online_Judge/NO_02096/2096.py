# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 2096 내려가기                       | #
# -------------------------------------- #


def run():
    N = int(r_input())

    max_dp = []
    min_dp = []

    for val in map(int, r_input().split()):
        max_dp.append(val)
        min_dp.append(val)

    for _ in range(N - 1):
        A, B, C = map(int, r_input().split())
        
        max_dp[0], max_dp[1], max_dp[2] = max(max_dp[:-1]) + A, max(max_dp) + B, max(max_dp[1:]) + C
        min_dp[0], min_dp[1], min_dp[2] = min(min_dp[:-1]) + A, min(min_dp) + B, min(min_dp[1:]) + C

    print(max(max_dp), min(min_dp))


if __name__ == "__main__":
    run()
