# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 10469 사이 나쁜 여왕들              | #
# -------------------------------------- #


if __name__ == "__main__":
    board = [list(r_input().rstrip()) for _ in range(8)]

    flag = 1

    for row in range(8):
        if board[row].count('*') != 1:
            flag = 0
            break

        for col in range(8):
            if board[row][col] == '*':
                
                for tmp_row in range(8):
                    if row != tmp_row and board[tmp_row][col] == '*':
                        flag = 0
                        break
                
                if not flag:
                    break

                for di in range(-7, 8):
                    tmp_row = row + di
                    tmp_col = col + di

                    if 0 <= tmp_row < 8 and 0 <= tmp_col < 8:
                        if (tmp_row, tmp_col) != (row, col) and board[tmp_row][tmp_col] == '*':
                            flag = 0
                            break
                    
                    tmp_row = row - di
                    tmp_col = col + di

                    if 0 <= tmp_row < 8 and 0 <= tmp_col < 8:
                        if (tmp_row, tmp_col) != (row, col) and board[tmp_row][tmp_col] == '*':
                            flag = 0
                            break
                
                if not flag:
                    break
    
    print(['invalid', 'valid'][flag])
