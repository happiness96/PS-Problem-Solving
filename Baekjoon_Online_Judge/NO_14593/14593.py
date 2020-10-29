# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 29                             | #
# | 14593 2017 아주대학교 프로그래밍 경시대회 (Large) | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    rank = []

    for st_no in range(1, N + 1):
        S, C, L = map(int, r_input().split())

        rank.append((-S, C, L, st_no))
    
    rank.sort()

    print(rank[0][-1])
