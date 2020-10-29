# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 29                             | #
# | 6146 신아를 만나러                  | #
# -------------------------------------- #


def run():
    X, Y, N = map(int, r_input().split())

    PLU = 501
    X += PLU
    Y += PLU

    board = [[0] * (PLU * 2) for _ in range(PLU * 2)]
    visit = [[0] * (PLU * 2) for _ in range(PLU * 2)]

    for _ in range(N):
        A, B = map(int, r_input().split())

        board[A + PLU][B + PLU] = 1

    queue = deque([(PLU, PLU)])
    visit[PLU][PLU] = 1
    dist = 0

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            
            if (row, col) == (X, Y):
                print(dist)
                sys.exit()

            for mv_row, mv_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tmp_row = row + mv_row
                tmp_col = col + mv_col

                if 0 <= tmp_row < PLU * 2 and 0 <= tmp_col < PLU * 2:
                    if not visit[tmp_row][tmp_col] and not board[tmp_row][tmp_col]:
                        visit[tmp_row][tmp_col] = 1
                        queue.append((tmp_row, tmp_col))
        
        dist += 1


if __name__ == "__main__":
    run()
