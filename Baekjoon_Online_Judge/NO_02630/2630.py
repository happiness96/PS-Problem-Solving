# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 2630 색종이 만들기                  | #
# -------------------------------------- #


def devide(x, y, size):
    global white, blue

    flag = 1
    block = board[x][y]

    for row in range(x, x + size):
        for col in range(y, y + size):
            if board[row][col] != block:
                flag = 0
                break
        
        if not flag:
            break
    
    if flag:
        if block == 0:
            white += 1
        
        else:
            blue += 1
    
    elif size != 1:
        new_size = size // 2

        devide(x, y, new_size)
        devide(x, y + new_size, new_size)
        devide(x + new_size, y, new_size)
        devide(x + new_size, y + new_size, new_size)


if __name__ == "__main__":
    N = int(r_input())
    board = [list(map(int, r_input().split())) for _ in range(N)]

    white = blue = 0

    devide(0, 0, N)

    print(white)
    print(blue)
