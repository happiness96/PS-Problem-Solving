# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 14397 해변                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in range(N)]
    cnt = 0

    for row in range(N):
        for col in range(M):
            if board[row][col] == '.':
                if row % 2:
                    mv = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1)]
                
                else:
                    mv = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1)]
                
                for mv_row, mv_col in mv:
                    tmp_row = row + mv_row
                    tmp_col = col + mv_col

                    if 0 <= tmp_row < N and 0 <= tmp_col < M:
                        if board[tmp_row][tmp_col] == '#':
                            cnt += 1
    
    print(cnt)
