# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19952 인성 문제 있어?                | #
# -------------------------------------- #


def run():
    T = int(r_input())

    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(T):
        H, W, O, F, SR, SC, DR, DC = map(int, r_input().split())
        SR -= 1
        SC -= 1
        DR -= 1
        DC -= 1

        board = [[0] * W for _ in range(H)]
        visit = [[-1] * W for _ in range(H)]

        dest_loc = (DR, DC)

        for _ in range(O):
            X, Y, L = map(int, r_input().split())

            board[X - 1][Y - 1] = L

        visit[SR][SC] = F

        queue = deque([(SR, SC, F)])

        flag = 0

        while queue:
            start_row, start_col, rem_F = queue.popleft()

            if start_row == DR and start_col == DC:
                flag = 1

            for mv_row, mv_col in mv:
                tmp_row = start_row + mv_row
                tmp_col = start_col + mv_col

                if 0 <= tmp_row < H and 0 <= tmp_col < W:
                    if rem_F > visit[tmp_row][tmp_col] + 1:
                        gap = board[tmp_row][tmp_col] - board[start_row][start_col]

                        if gap <= 0 or gap <= rem_F:
                            queue.append((tmp_row, tmp_col, rem_F - 1))
                            visit[tmp_row][tmp_col] = rem_F - 1
        
        print(['인성 문제있어??', '잘했어!!'][flag])


if __name__ == "__main__":
    run()
