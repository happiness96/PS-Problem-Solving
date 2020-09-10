# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 10                             | #
# | 14039 Magic Squares                | #
# -------------------------------------- #


def run():
    squares = [list(map(int, r_input().split())) for _ in range(4)]

    tot = sum(squares[0])

    for row in range(4):
        tmp_tot = sum(squares[row])

        if tmp_tot != tot:
            print('not magic')
            sys.exit()
        
    for col in range(4):
        tmp_tot = 0

        for row in range(4):
            tmp_tot += squares[row][col]
        
        if tmp_tot != tot:
            print('not magic')
            sys.exit()
    
    print('magic')


if __name__ == "__main__":
    run()
