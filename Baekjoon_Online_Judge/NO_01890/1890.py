# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 28                   | #
# | 1890 점프                | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    board = [list(map(int, r_input().split())) for _ in range(N)]
    save = [[0] * N for _ in range(N)]

    save[0][0] = 1

    for row in range(N):
        for col in range(N):
            row_mv = row + board[row][col]
            col_mv = col + board[row][col]
            
            if row_mv < N:
                save[row_mv][col] += save[row][col]

            if col_mv < N:
                save[row][col_mv] += save[row][col]

    print(save[-1][-1] // 2 // 2)
