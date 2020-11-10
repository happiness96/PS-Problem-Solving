# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 10                             | #
# | 14235 크리스마스 선물               | #
# -------------------------------------- #


def run():
    n = int(r_input())
    
    present = []

    for _ in range(n):
        a, *values = list(map(int, r_input().split()))
        
        for val in values:
            heappush(present, -val)
        
        if not a:
            print(-heappop(present) if present else -1)


if __name__ == "__main__":
    run()
