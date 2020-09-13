# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 13                             | #
# | 17212 달나라 토끼를 위한 구매대금 지불 도우미 | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    dp = [sys.maxsize] * (max(8, N + 1))
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[5] = 1
    dp[7] = 1

    for cost in range(1, N + 1):
        for coin in [1, 2, 5, 7]:
            tmp_cost = cost + coin
            
            if tmp_cost > N:
                break

            dp[tmp_cost] = min(dp[tmp_cost], dp[cost] + 1)
            
    print(dp[N])
