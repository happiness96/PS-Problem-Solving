# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 26                             | #
# | 3709 레이저빔은 어디로              | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for _ in range(T):
        n, r = map(int, r_input().split())

        board = [[0] * (n + 2) for _ in range(n + 2)]
        visit = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(4)]

        for _ in range(r):
            x, y = map(int, r_input().split())

            board[x][y] = 1
        
        X, Y = map(int, r_input().split())

        if X == 0:
            direction = 2
        
        elif Y == 0:
            direction = 1
        
        elif X == n + 1:
            direction = 0
        
        else:
            direction = 3
        
        while True:
            mv_X, mv_Y = mv[direction]

            X += mv_X
            Y += mv_Y

            if board[X][Y]:
                direction = (direction + 1) % 4
            
            if 0 in (X, Y) or n + 1 in (X, Y):
                print(X, Y)
                break

            if visit[direction][X][Y]:
                print(0, 0)
                break
        
            visit[direction][X][Y] = 1
