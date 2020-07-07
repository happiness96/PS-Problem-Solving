# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 07                   | #
# | 15722 빙글빙글 스네일       | #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    mv = 1
    flag = 0

    row, col = 0, 0
    
    while True:
        for mv_row, mv_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if n - mv < 0:
                print(row + mv_row * n, col + mv_col * n)
                sys.exit()

            row, col = row + mv_row * mv, col + mv_col * mv
            n -= mv
            
            if flag:
                flag = 0
                mv += 1
            
            else:
                flag = 1
