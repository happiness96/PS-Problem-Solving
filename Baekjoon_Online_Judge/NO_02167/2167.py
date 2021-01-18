# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 18                             | #
# | 2167 2차원 배열의 합                | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    board = [list(map(int, r_input().split())) for _ in range(N)]

    K = int(r_input())

    for _ in range(K):
        i, j, x, y = map(int, r_input().split())
        i -= 1
        j -= 1
        tot = 0

        for row in range(i, x):
            for col in range(j, y):
                tot += board[row][col]

        print(tot)


if __name__ == "__main__":
    run()
