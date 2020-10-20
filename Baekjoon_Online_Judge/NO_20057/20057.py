# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 20057 마법사 상어와 토네이도         | #
# -------------------------------------- #


def run():
    N = int(r_input())

    board = [list(map(int, r_input().split())) for _ in range(N)]
    row, col = (N // 2, N // 2)
    direction = 0

    mv = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    split = [
    {0.05: [(0, -2)], 0.1: [(1, -1), (-1, -1)], 0.02: [(-2, 0), (2, 0)], 0.07:[(-1, 0), (1, 0)], 0.01: [(1, 1), (-1, 1)]},
    {0.05: [(2, 0)], 0.1: [(1, -1), (1, 1)], 0.02: [(0, -2), (0, 2)], 0.07:[(0, -1), (0, 1)], 0.01: [(-1, 1), (-1, -1)]},
    {0.05: [(0, 2)], 0.1: [(1, 1), (-1, 1)], 0.02: [(-2, 0), (2, 0)], 0.07:[(-1, 0), (1, 0)], 0.01: [(-1, -1), (1, -1)]},
    {0.05: [(-2, 0)], 0.1: [(-1, -1), (-1, 1)], 0.02: [(0, -2), (0, 2)], 0.07:[(0, -1), (0, 1)], 0.01: [(1, 1), (1, -1)]}
    ]
    out = 0

    for go in range(1, N):
        loop = 3 if go == N - 1 else 2

        for _ in range(loop):
            for _ in range(go):
                mv_row, mv_col = mv[direction]
                row += mv_row
                col += mv_col

                sand = board[row][col]

                for rate, split_loc_list in split[direction].items():
                    for split_loc in split_loc_list:
                        split_row, split_col = split_loc

                        tmp_row = row + split_row
                        tmp_col = col + split_col

                        mv_sand = int(sand * rate)

                        if 0 <= tmp_row < N and 0 <= tmp_col < N:
                            board[tmp_row][tmp_col] += mv_sand

                        else:
                            out += mv_sand
                        
                        board[row][col] -= mv_sand
                
                alpha_row, alpha_col = row + mv_row, col + mv_col

                if 0 <= alpha_row < N and 0 <= alpha_col < N:
                    board[alpha_row][alpha_col] += board[row][col]
                
                else:
                    out += board[row][col]
                
                board[row][col] = 0
                
            direction = (direction + 1) % 4
    
    print(out)


if __name__ == "__main__":
    run()
