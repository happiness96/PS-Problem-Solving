# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 16946 벽 부수고 이동하기 4  | #
# ---------------------------- #


def run():
    N, M = map(int, r_input().split())
    board = [list(r_input().rstrip()) for _ in range(N)]

    visit = [[0] * M for _ in range(N)]
    save = [[(0, 0)] * M for _ in range(N)]
    hole_num = 1

    for row in range(N):
        for col in range(M):
            if not visit[row][col]:
                if board[row][col] == '0':
                    edge = set()
                    size = 1
                    visit[row][col] = 1
                    queue = deque([(row, col)])

                    while queue:
                        r, c = queue.popleft()

                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            tmp_row = r + dx
                            tmp_col = c + dy

                            if 0 <= tmp_row < N and 0 <= tmp_col < M:
                                if not visit[tmp_row][tmp_col]:
                                    if board[tmp_row][tmp_col] == '1':
                                        edge.add((r, c))
                                    else:
                                        queue.append((tmp_row, tmp_col))
                                        visit[tmp_row][tmp_col] = 1
                                        size += 1
                    
                    for edge_row, edge_col in edge:
                        save[edge_row][edge_col] = (hole_num, size)

                    hole_num += 1

    for row in range(N):
        for col in range(M):
            if board[row][col] == '1':
                tmp = set()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tmp_row = row + dx
                    tmp_col = col + dy

                    if 0 <= tmp_row < N and 0 <= tmp_col < M:
                        tmp.add(save[tmp_row][tmp_col])
                
                tot = 1

                for _, val in tmp:
                    tot += val
                
                print(tot % 10, end='')
            
            else:
                print(0, end='')
        
        print()


if __name__ == "__main__":
    run()
