# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 25                             | #
# | 9095 1, 2, 3 더하기                | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    dp = [0] * 11

    for i in range(1, 11):
        if i in (1, 2, 3):
            dp[i] += 1
            
        dp[i] += dp[i - 1]
        
        if i > 1:
            dp[i] += dp[i - 2]
        
        if i > 2:
            dp[i] += dp[i - 3]

    for _ in range(T):
        n = int(r_input())

        print(dp[n])
