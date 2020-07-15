# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 2897 몬스터 트럭           | #
# ---------------------------- #


if __name__ == "__main__":
    R, C = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in  range(R)]

    res = [0] * 5

    for row in range(R - 1):
        for col in range(C - 1):
            tmp = board[row][col] + board[row][col + 1] + board[row + 1][col] + board[row + 1][col + 1]

            if '#' not in tmp:
                res[tmp.count('X')] += 1
    
    print(*res, sep='\n')
