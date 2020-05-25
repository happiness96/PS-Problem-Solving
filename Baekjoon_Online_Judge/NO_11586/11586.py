# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 11586 지영 공주님의 마법 거울| #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    mirror = [r_input().rstrip() for _ in range(N)]

    K = int(r_input())

    if K == 1:
        for m in mirror:
            print(m)
    
    elif K == 2:
        for m in mirror:
            print(m[::-1])
    
    else:
        for m in reversed(mirror):
            print(m)
