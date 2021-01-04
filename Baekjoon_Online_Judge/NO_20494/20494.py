# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 20494 스시                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    result = 0

    for _ in range(N):
        result += len(r_input().rstrip())
    
    print(result)
