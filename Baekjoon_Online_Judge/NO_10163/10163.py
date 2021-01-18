# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 18                             | #
# | 10163 색종이                       | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    board = [[0] * 103 for _ in range(103)]

    for paper_no in range(1, N + 1):
        x, y, w, h = map(int, r_input().split())

        for row in range(x, x + h):
            for col in range(y, y + w):
                board[row][col] = paper_no

    for paper_no in range(1, N + 1):
        tot = 0

        for b in board:
            tot += b.count(paper_no)
        
        print(tot)
