# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 30                   | #
# | 14497 주난의 난(難)        | #
# ---------------------------- #


def run():
    N, M = map(int, r_input().split())
    x1, y1, x2, y2 = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in range(N)]

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    cnt = 0

    while True:
        queue = deque([(x1, y1)])
        visit = [[0] * M for _ in range(N)]

        visit[x1][y1] = 1

        while queue:
            x, y = queue.popleft()

            if (x, y) == (x2, y2):
                print(cnt + 1)
                sys.exit()

            for dx,dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tmp_x = x + dx
                tmp_y = y + dy

                if 0 <= tmp_x < N and 0 <= tmp_y < M:
                    if not visit[tmp_x][tmp_y]:
                        visit[tmp_x][tmp_y] = 1

                        if board[tmp_x][tmp_y] == '1':
                            board[tmp_x][tmp_y] = '0'

                        else:
                            queue.append((tmp_x, tmp_y))
        
        cnt += 1


if __name__ == "__main__":
    run()
