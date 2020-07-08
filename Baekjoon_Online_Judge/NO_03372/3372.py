# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 3372 보드 점프            | #
# ---------------------------- #


def run():
    N = int(r_input())

    dp = [[0] * N for _ in range(N)]
    board = [list(map(int, r_input().split())) for _ in range(N)]

    dp[0][0] = 1

    for row in range(N):
        for col in range(N):
            mv = board[row][col]
            
            if not mv:
                continue

            tmp_row = row + mv
            tmp_col = col + mv

            if tmp_row < N:
                dp[tmp_row][col] += dp[row][col]
            
            if tmp_col < N:
                dp[row][tmp_col] += dp[row][col]
    
    print(dp[-1][-1])


if __name__ == "__main__":
    run()
