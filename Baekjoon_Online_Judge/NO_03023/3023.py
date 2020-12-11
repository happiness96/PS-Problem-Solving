# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 11                             | #
# | 3023 마술사 이민혁                 | #
# -------------------------------------- #


if __name__ == "__main__":
    R, C = map(int, r_input().split())

    board = [list(r_input().rstrip()) for _ in range(R)]
    err_R, err_C = map(int, r_input().split())

    result = []

    for row in range(R):
        result.append(board[row] + board[row][::-1])
    
    for row in range(R - 1, -1, -1):
        result.append(board[row] + board[row][::-1])
    
    err_R -= 1
    err_C -= 1
    
    if result[err_R][err_C] == '.':
        result[err_R][err_C] = '#'
    
    else:
        result[err_R][err_C] = '.'

    for r in result:
        print(''.join(r))
