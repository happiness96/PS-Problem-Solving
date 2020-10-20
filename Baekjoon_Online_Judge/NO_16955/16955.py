# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 16955 오목, 이길 수 있을까?          | #
# -------------------------------------- #


def run():
    board = [list(r_input().rstrip()) for _ in range(10)]

    for row in range(10):
        for col in range(10):
            if board[row][col] == '.':
                board[row][col] = 'X'

                tmp1 = ''.join(board[row])
                tmp2 = ''
                tmp3 = ''
                tmp4 = ''

                for tmp_row in range(10):
                    tmp2 += board[tmp_row][col]
                
                for k in range(-9, 10):
                    tmp_row, tmp_col = row + k, col + k

                    if 0 <= tmp_row < 10 and 0 <= tmp_col < 10:
                        tmp3 += board[tmp_row][tmp_col]
                    
                    tmp_row, tmp_col = row - k, col + k

                    if 0 <= tmp_row < 10 and 0 <= tmp_col < 10:
                        tmp4 += board[tmp_row][tmp_col]
                
                for check in [tmp1, tmp2, tmp3, tmp4]:
                    if 'XXXXX' in check:
                        print(1)
                        sys.exit()

                board[row][col] = '.'

    print(0)


if __name__ == "__main__":
    run()
