# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 28                             | #
# | 18821 교수님 저는 취업할래요        | #
# -------------------------------------- #


def run():
    N = int(r_input())

    board = []
    row_list = []
    col_list = []

    for row in range(N):
        line = list(map(int, r_input().split()))

        for col, val in enumerate(line):
            if val in (2, 5):
                row_list.append(row)
                col_list.append(col)
        
        board.append(line)
    
    if ((row_list[0] - row_list[1]) ** 2 + (col_list[0] - col_list[1]) ** 2) ** 0.5 < 5:
        print(0)
        sys.exit()
    
    cnt = 0

    for row in range(min(row_list), max(row_list) + 1):
        for col in range(min(col_list), max(col_list) + 1):
            if board[row][col] == 1:
                cnt += 1
    
    print(0 if cnt < 3 else 1)


if __name__ == "__main__":
    run()
