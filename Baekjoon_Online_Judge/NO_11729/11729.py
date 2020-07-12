# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 29                   | #
# | 11729 하노이 탑 이동 순서   | #
# ---------------------------- #


def hanoi(count, start, mid, dest):
    if count == 1:
        print(start, dest)
    
    else:
        hanoi(count - 1, start, dest, mid)
        print(start, dest)
        hanoi(count - 1, mid, start, dest)
    

if __name__ == "__main__":
    N = int(r_input())

    print(2 ** N - 1)

    hanoi(N, 1, 2, 3)
