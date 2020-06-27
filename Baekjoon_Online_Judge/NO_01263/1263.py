# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 1263 시간 관리            | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    T = {}

    for _ in range(N):
        Si, Ti = map(int, r_input().split())
        
        if Ti not in T:
            T[Ti] = 0
        
        T[Ti] += Si
    
    cur = max(T)

    for t in sorted(T, reverse=True):
        cur = min(t, cur)
        cur -= T[t]

    print(max(-1, cur))
