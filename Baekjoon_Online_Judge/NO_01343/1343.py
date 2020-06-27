# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 1343 폴리오미노            | #
# ---------------------------- #


if __name__ == "__main__":
    board = r_input().rstrip()

    board = board.replace('XXXX', 'AAAA')
    board = board.replace('XX', 'BB')

    if 'X' in board:
        print(-1)
    
    else:
        print(board)
