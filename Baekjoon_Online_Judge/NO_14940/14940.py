# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 05                             | #
# | 14940 쉬운 최단거리                 | #
# -------------------------------------- #


def run():
    n, m = map(int, r_input().split())

    start_row = start_col = 0
    board = []
    visit = [[0] * m for _ in range(n)]

    for row in range(n):
        line = list(map(int, r_input().split()))

        for col, val in enumerate(line):
            if val == 2:
                start_row = row
                start_col = col
                visit[row][col] = 1
            
        board.append(line)
    
    queue = deque([(start_row, start_col)])
    dist = 1

    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            for dr, dc in mv:
                tmp_row = row + dr
                tmp_col = col + dc

                if 0 <= tmp_row < n and 0 <= tmp_col < m:
                    if not visit[tmp_row][tmp_col] and board[tmp_row][tmp_col] == 1:
                        queue.append((tmp_row, tmp_col))
                        visit[tmp_row][tmp_col] = dist

        dist += 1

    for row in range(n):
        for col in range(m):
            if board[row][col] != 0 and visit[row][col] == 0:
                visit[row][col] = -1
    
    visit[start_row][start_col] = 0

    for line in visit:
        print(*line)


if __name__ == "__main__":
    run()
