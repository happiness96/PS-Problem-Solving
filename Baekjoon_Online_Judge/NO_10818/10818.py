# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 최소, 최대                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    mini = 1000000
    maxi = -1000000

    for val in map(int, r_input().split()):
        mini = min(mini, val)
        maxi = max(maxi, val)
    
    print(mini, maxi)
