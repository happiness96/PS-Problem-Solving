# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 18                             | #
# | 9655 돌 게임                        | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    dp = [1] * 1001

    # 상근이가 이기는 경우 0
    # 창영이가 이기는 경우 1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 0
    
    for ind in range(4, 1001):
        if dp[ind - 1] == dp[ind - 3] == 1:
            dp[ind] = 0
        
    print(['SK', 'CY'][dp[N]])
