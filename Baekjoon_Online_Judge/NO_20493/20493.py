# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 20493 세상은 하나의 손수건          | #
# -------------------------------------- #


def run():
    N, T = map(int, r_input().split())

    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 2
    x = y = 0
    time = 0

    for _ in range(N):
        Ti, Si = map(str, r_input().rstrip().split())
        Ti = int(Ti)
        tmp = Ti - time

        mv_x, mv_y = mv[d]

        x += mv_x * tmp
        y += mv_y * tmp

        if Si == 'right':
            d = (d + 1) % 4
        
        else:
            d = (d - 1) % 4
        
        time = Ti
    
    tmp = T - time
    
    mv_x, mv_y = mv[d]
    x += mv_x * tmp
    y += mv_y * tmp

    print(x, y)


if __name__ == "__main__":
    run()
