# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 18                             | #
# | 16768 Mooyo Mooyo                  | #
# -------------------------------------- #


if __name__ == "__main__":
    N, K = map(int, r_input().split())

    board = [list(map(int, list(r_input().rstrip()))) for _ in range(N)]
    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while True:
        visit = [[0] * 10 for _ in range(N)]

        flag = 0

        for row in range(N):
            for col in range(10):
                if not visit[row][col]:
                    visit[row][col] = 1

                    if board[row][col] != 0:
                        save = [(row, col)]
                        queue = [(row, col)]
                        comp = board[row][col]

                        while queue:
                            r, c = queue.pop()

                            for mv_r, mv_c in mv:
                                tmp_r = r + mv_r
                                tmp_c = c + mv_c
                                
                                if 0 <= tmp_r < N and 0 <= tmp_c < 10:
                                    if not visit[tmp_r][tmp_c] and board[tmp_r][tmp_c] == comp:
                                        visit[tmp_r][tmp_c] = 1
                                        save.append((tmp_r, tmp_c))
                                        queue.append((tmp_r, tmp_c))
                        
                        if len(save) >= K:
                            flag = 1

                            for r, c in save:
                                board[r][c] = 0
        
        if not flag:
            break

        for col in range(10):
            switch_loc = N - 1

            for row in range(N - 1, -1, -1):
                if board[row][col] != 0:
                    board[row][col], board[switch_loc][col] = board[switch_loc][col], board[row][col]
                    switch_loc -= 1

    for b in board:
        print(*b, sep='')
