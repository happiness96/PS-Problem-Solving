# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 10797 10부제              | #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())
    res = 0

    for num in map(int, r_input().split()):
        if num == n:
            res += 1
    
    print(res)
