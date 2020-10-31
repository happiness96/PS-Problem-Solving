# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 1138 한 줄로 서기                    | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    taller = list(map(int, r_input().split()))
    
    res = []

    for ind in range(N - 1, -1, -1):
        res.insert(taller[ind], ind + 1)
    
    print(*res)
