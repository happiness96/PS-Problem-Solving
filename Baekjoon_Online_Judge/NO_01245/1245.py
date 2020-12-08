# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 08                             | #
# | 1245 농장 관리                      | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    board = [list(map(int, r_input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    result = 0
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for row in range(N):
        for col in range(M):
            if board[row][col] and not visit[row][col]:
                visit[row][col] = 1
                val = board[row][col]
                save = []
                queue = [(row, col)]

                while queue:
                    r, c = queue.pop()
                    save.append((r, c))

                    for mv_row, mv_col in mv:
                        tmp_row = r + mv_row
                        tmp_col = c + mv_col

                        if 0 <= tmp_row < N and 0 <= tmp_col < M:
                            if not visit[tmp_row][tmp_col] and board[tmp_row][tmp_col] == val:
                                queue.append((tmp_row, tmp_col))
                                visit[tmp_row][tmp_col] = 1
                
                flag = 1

                for r, c in save:
                    for mv_row, mv_col in mv:
                        tmp_row = r + mv_row
                        tmp_col = c + mv_col

                        if 0 <= tmp_row < N and 0 <= tmp_col < M:
                            if board[tmp_row][tmp_col] > val:
                                flag = 0
                                break
                    
                    if not flag:
                        break
                
                result += flag

    print(result)


if __name__ == "__main__":
    run()
