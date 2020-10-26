# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 26                             | #
# | 2823 유턴 싫어                      | #
# -------------------------------------- #


def run():
    R, C = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in range(R)]

    mv = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    for row in range(R):
        for col in range(C):
            if board[row][col] == '.':
                cnt = 0

                for mv_row, mv_col in mv:
                    tmp_row = row + mv_row
                    tmp_col = col + mv_col

                    if 0 <= tmp_row < R and 0 <= tmp_col < C:
                        if board[tmp_row][tmp_col] == '.':
                            cnt += 1
                
                if cnt == 1:
                    print(1)
                    sys.exit()

    print(0)


if __name__ == "__main__":
    run()
