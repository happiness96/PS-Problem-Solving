# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 28                             | #
# | 1931 회의실 배정                    | #
# -------------------------------------- #


def run():
    N = int(r_input())

    save = []

    for _ in range(N):
        start, end = map(int, r_input().split())
        save.append((start, end))
    
    save.sort()
    
    cnt = 0
    last = 0
    
    for s, e in save:
        if s >= last:
            last = e
            cnt += 1
        
        elif e < last:
            last = e
    
    print(cnt)
        

if __name__ == "__main__":
    run()
