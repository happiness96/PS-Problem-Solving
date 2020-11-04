# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 05                             | #
# | 14568 2017 연세대학교 프로그래밍 경시대회| #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    res = 0

    for A in range(2, N, 2):
        for B in range(1, N - A + 1):
            for C in range(B + 2, N - A - B + 1):
                res += 1
                break
    
    print(res)
