# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 1912 연속합               | #
# ---------------------------- #


def run():
    n = int(r_input())
    A = list(map(int, r_input().split()))
    dp = [-1000] * n

    for ind, val in enumerate(A):
        if ind == 0:
            dp[ind] = val
        
        else:
            dp[ind] = max(dp[ind - 1] + val, val)
    
    print(max(dp))


if __name__ == "__main__":
    run()
