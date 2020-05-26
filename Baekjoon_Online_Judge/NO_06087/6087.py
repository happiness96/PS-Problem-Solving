# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 26                   | #
# | 6087 레이저 통신           | #
# ---------------------------- #


def run():
    W, H = map(int, r_input().split())

    board = []
    start = ()
    end = ()

    for row in range(H):
        line = list(r_input().rstrip())

        for col in range(W):
            if line[col] == 'C':
                line[col] = '.'

                if start:
                    end = (row, col)
                
                else:
                    start = (row, col)
        
        board.append(line)
    
    queue = deque()

    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for mv in range(4):
        queue.append((start[0], start[1], mv, 0))
    
    INF = sys.maxsize
    visit = [[INF] * W for _ in range(H)]

    visit[start[0]][start[1]] = 0

    while queue:
        row, col, direction, count = queue.popleft()

        if (row, col) == end:
            continue

        straight_row = row + move[direction][0]
        straight_col = col + move[direction][1]

        if 0 <= straight_row < H and 0 <= straight_col < W:
            if board[straight_row][straight_col] != '*':
                if count <= visit[straight_row][straight_col]:
                    visit[straight_row][straight_col] = count
                    queue.append((straight_row, straight_col, direction, count))
        
        left_direction = direction - 1
        
        if left_direction == -1:
            left_direction = 3
        
        left_row = row + move[left_direction][0]
        left_col = col + move[left_direction][1]

        if 0 <= left_row < H and 0 <= left_col < W:
            if board[left_row][left_col] != '*':
                if count + 1 <= visit[left_row][left_col]:
                    visit[left_row][left_col] = count + 1
                    queue.append((left_row, left_col, left_direction, count + 1))
        
        right_direction = direction + 1

        if right_direction == 4:
            right_direction = 0
        
        right_row = row + move[right_direction][0]
        right_col = col + move[right_direction][1]

        if 0 <= right_row < H and 0 <= right_col < W:
            if board[right_row][right_col] != '*':
                if count + 1 <= visit[right_row][right_col]:
                    visit[right_row][right_col] = count + 1
                    queue.append((right_row, right_col, right_direction, count + 1))
    
    print(visit[end[0]][end[1]])


if __name__ == "__main__":
    run()
