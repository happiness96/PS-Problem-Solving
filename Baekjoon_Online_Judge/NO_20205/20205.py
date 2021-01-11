# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 11                             | #
# | 20205 교수님 그림이 깨지는데요?     | #
# -------------------------------------- #


if __name__ == "__main__":
    N, K = map(int, r_input().split())

    board = [list(map(int, r_input().split())) for _ in range(N)]

    for i in range(N):
        for _ in range(K):
            for j in range(N):
                block = board[i][j]

                for _ in range(K):
                    print(block, end=' ')
                
            print()
