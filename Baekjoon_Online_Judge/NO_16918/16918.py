# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 29                   | #
# | 16918 봄버맨              | #
# ---------------------------- #


def run():
    R, C, N = map(int, r_input().split())

    board = []
    rem = [[0] * C for _ in range(R)]

    for row in range(R):
        line = list(r_input().rstrip())

        for col in range(C):
            if line[col] == 'O':
                rem[row][col] = 2
        
        board.append(line)
    
    N -= 1

    while N > 4:
        N -= 4
    
    for ind in range(N):
        if ind % 2:
            for row in range(R):
                for col in range(C):
                    if rem[row][col] == 1:
                        board[row][col] = '.'

                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            tmp_row = row + dr
                            tmp_col = col + dc

                            if 0 <= tmp_row < R and 0 <= tmp_col < C:
                                if rem[tmp_row][tmp_col] != 1:
                                    board[tmp_row][tmp_col] = '.'
                                    rem[tmp_row][tmp_col] = 0


        else:
            for row in range(R):
                for col in range(C):
                    if not rem[row][col]:
                        rem[row][col] = 4
                        board[row][col] = 'O'
        

        for row in range(R):
            for col in range(C):
                rem[row][col] = max(rem[row][col] - 1, 0)
    
    for b in board:
        print(*b, sep='')


if __name__ == "__main__":
    run()
