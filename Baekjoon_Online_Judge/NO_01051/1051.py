# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 03                             | #
# | 1051 숫자 정사각형                 | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    res = 1

    board = [list(r_input().rstrip()) for _ in range(N)]

    for row in range(N):
        for col in range(M):
            for k in range(res, min(N - row, M - col)):
                if board[row][col] == board[row][col + k] == board[row + k][col] == board[row + k][col + k]:                    
                    res = k + 1
                    
    print(res ** 2)


if __name__ == "__main__":
    run()
