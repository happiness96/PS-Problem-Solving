# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 14                   | #
# | 18247 겨울왕국 티켓 예매    | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        N, M = map(int, r_input().split())

        if N < 12 or M < 4:
            print(-1)
        
        else:
            print(M * 11 + 4)
