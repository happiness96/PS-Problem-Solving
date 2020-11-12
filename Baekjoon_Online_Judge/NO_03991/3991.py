# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 12                             | #
# | 3991 한번 쏘면 멈출 수 없어         | #
# -------------------------------------- #


if __name__ == "__main__":
    h, w, c = map(int, r_input().split())

    color_count = [0] + list(map(int, r_input().split()))
    board = [[0] * w for _ in range(h)]

    col_move = 1
    row, col = 0, 0

    for num, cnt in enumerate(color_count):
        for _ in range(cnt):
            if not 0 <= col < w:
                row += 1
                col_move = -col_move
                col += col_move
            
            board[row][col] = str(num)
            col += col_move
    
    for b in board:
        print(''.join(b))
