# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 29                             | #
# | 1246 온라인 판매                    | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    P = [int(r_input()) for _ in range(M)]
    P.sort(reverse=True)

    price = 0
    profit = 0

    for i in range(min(N, M)):
        pr = P[i]

        tot = pr * (i + 1)

        if tot >= profit:
            profit = tot
            price = pr
    
    print(price, profit)
