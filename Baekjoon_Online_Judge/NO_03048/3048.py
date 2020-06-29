# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 29                   | #
# | 3048 개미                | #
# ---------------------------- #


if __name__ == "__main__":
    N1, N2 = map(int, r_input().split())

    ant1 = list(r_input().rstrip())
    ant2 = list(reversed(r_input().rstrip()))

    T = int(r_input())
    
    start1 = 0
    start2 = N1

    if start2 >= T:
        start2 -= T
    
    else:
        T -= start2
        start2 = 0
        start1 = min(T, N2)

    for ind in range(N1 + N2 + 1):
        if ind >= start2:
            if ant2:
                print(ant2.pop(), end='')
        
        if ind >= start1:
            if ant1:
                print(ant1.pop(), end='')
