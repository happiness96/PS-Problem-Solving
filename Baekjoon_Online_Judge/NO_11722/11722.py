# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 25                   | #
# | 11722 가장 긴 감소하는 부분 수열| #
# ---------------------------- #


def run():
    N = int(r_input())

    dp = [0] * 1002

    for value in map(int, r_input().split()):
        dp[value] = max(dp[value], max(dp[value + 1:]) + 1)
    
    print(max(dp))


if __name__ == "__main__":
    run()
