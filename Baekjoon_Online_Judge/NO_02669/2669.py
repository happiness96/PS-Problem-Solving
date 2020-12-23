# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 23                             | #
# | 2669 직사각형 네개의 합집합의 면적 구하기| #
# -------------------------------------- #


if __name__ == "__main__":
    board = [[0] * 101 for _ in range(101)]

    for _ in range(4):
        x1, y1, x2, y2 = map(int, r_input().split())

        for y in range(y1, y2):
            for x in range(x1, x2):
                board[y][x] = 1
    
    total = 0

    for b in board:
        total += sum(b)
    
    print(total)
