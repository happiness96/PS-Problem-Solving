# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 18242 네모네모 시력검사     | #
# ---------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())
    board = [r_input().rstrip() for _ in range(N)]

    up = down = left = right = 0

    for row in range(N):
        if '#' in board[row]:
            up = board[row].count('#')
            break
    
    for row in range(N - 1, -1, -1):
        if '#' in board[row]:
            down = board[row].count('#')
            break
    
    for col in range(M):
        for row in range(N):
            left += int(board[row][col] == '#')
        
        if left:
            break
    
    for col in range(M - 1, -1, -1):
        for row in range(N):
            right += int(board[row][col] == '#')
        
        if right:
            break
    
    if up != down == left == right:
        print('UP')
    
    elif down != up == left == right:
        print('DOWN')
    
    elif right != up == down == left:
        print('RIGHT')
    
    else:
        print('LEFT')