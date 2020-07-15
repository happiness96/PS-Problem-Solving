# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 2828 사과 담기 게임        | #
# ---------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())
    J = int(r_input())

    left, right = 1, M
    res = 0

    for _ in range(J):
        loc = int(r_input())

        if left <= loc <= right:
            continue

        if loc > right:
            mv = loc - right
            res += mv

            left += mv
            right += mv

        elif loc < left:
            mv = left - loc
            res += mv
            
            left -= mv
            right -= mv
    
    print(res)
