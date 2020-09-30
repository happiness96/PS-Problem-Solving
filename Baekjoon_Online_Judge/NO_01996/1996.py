# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 30                             | #
# | 1996 지뢰 찾기                     | #
# -------------------------------------- #


def run():
    N = int(r_input())
    board = [list(r_input().rstrip()) for _ in range(N)]

    mv = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for row in range(N):
        for col in range(N):
            if board[row][col] != '.':
                print('*', end='')
            
            else:
                tot = 0
                
                for mv_row, mv_col in mv:
                    tmp_row = row + mv_row
                    tmp_col = col + mv_col

                    if 0 <= tmp_row < N and 0 <= tmp_col < N:
                        if board[tmp_row][tmp_col] != '.':
                            tot += int(board[tmp_row][tmp_col])
                
                print('M' if tot >= 10 else tot, end='')
        
        print()


if __name__ == "__main__":
    run()
