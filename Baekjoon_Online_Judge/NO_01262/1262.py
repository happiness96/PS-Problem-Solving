# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 07                             | #
# | 1262 알파벳 다이아몬드               | #
# -------------------------------------- #


if __name__ == "__main__":
    N, R1, C1, R2, C2 = map(int, r_input().split())
    size = 2 * N - 1
    mid = size // 2
    cmp = mid * 2

    for row in range(R1, R2 + 1):
        for col in range(C1, C2 + 1):
            row_ind = row % size
            col_ind = col % size
            
            dist = abs(mid - row_ind) + abs(mid - col_ind)

            print(chr(97 + dist % 26) if dist < N else '.', end='')
        
        print()
