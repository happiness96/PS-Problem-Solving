# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 14925 목장 건설하기                 | #
# -------------------------------------- #


def run():
    M, N = map(int, r_input().split())

    pasture = [list(map(int, r_input().split())) for _ in range(M)]
    dp = [[0] * N for _ in range(M)]

    res = 0

    for row in range(M):
        if row + res >= M:
            break
        
        for col in range(N):
            if pasture[row][col]:
                continue
            
            if row == 0 or col == 0:
                dp[row][col] = 1
            
            else:
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1

    for d in dp:
        res = max(res, max(d))
    
    print(res)


if __name__ == "__main__":
    run()
