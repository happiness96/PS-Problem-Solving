# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 06                             | #
# |                           | #
# -------------------------------------- #


def N_and_M(node, save):
    if len(save) == M:
        print(*save)
        return
    
    for numbrer in range(1, N + 1):
        if number in save:
            continue
        
        else:
            N_and_M(number, save + [number])


if __name__ == "__main__": 
    N, M = map(int, r_input().split())

    for start in range(1, N + 1):
        N_and_M(start, [start])
