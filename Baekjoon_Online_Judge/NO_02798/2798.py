# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 14                             | #
# | 2798 블랙잭                        | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())
    cards = list(map(int, r_input().split()))

    result = 0

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                total = cards[i] + cards[j] + cards[k]
                
                if result < total <= M:
                    result = total
    
    print(result)
