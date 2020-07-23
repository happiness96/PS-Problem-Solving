# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 14916 거스름돈             | #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    res = sys.maxsize
    five = 0

    while five <= n:
        rem = n - five

        if rem % 2 == 0:
            total = five // 5 + rem // 2

            res = min(res, total)
        
        five += 5
    
    print(-1 if res == sys.maxsize else res)
