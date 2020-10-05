# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 05                             | #
# | 17129 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유 | #
# -------------------------------------- #


def run():
    n, m = map(int, r_input().split())

    board = [r_input().rstrip() for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    start_row = start_col = 0
    
    for row in range(n):
        for col in range(m):
            if board[row][col] == '2':
                start_row = row
                start_col = col
                visit[row][col] = 1
    
    queue = deque([(start_row, start_col)])
    dist = 1
    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            for mv_row, mv_col in mv:
                tmp_row = row + mv_row
                tmp_col = col + mv_col

                if 0 <= tmp_row < n and 0 <= tmp_col < m:
                    if not visit[tmp_row][tmp_col]:
                        visit[tmp_row][tmp_col] = 1

                        if board[tmp_row][tmp_col] == '1':
                            continue

                        queue.append((tmp_row, tmp_col))

                        if board[tmp_row][tmp_col] in '345':
                            print('TAK')
                            print(dist)
                            sys.exit()
        
        dist += 1
    
    print('NIE')


if __name__ == "__main__":
    run()
