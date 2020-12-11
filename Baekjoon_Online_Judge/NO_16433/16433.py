# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 11                             | #
# | 16433 주디와 당근농장               | #
# -------------------------------------- #


if __name__ == "__main__":
    N, R, C = map(int, r_input().split())

    board = [['.' for _ in range(N)] for _ in range(N)]
    R -= 1
    C -= 1

    for row in range(R % 2, N, 2):
        for col in range(C % 2, N, 2):
            board[row][col] = 'v'
    
    for row in range((R + 1) % 2, N, 2):
        for col in range((C + 1) % 2, N, 2):
            board[row][col] = 'v'

    for b in board:
        print(''.join(b))
