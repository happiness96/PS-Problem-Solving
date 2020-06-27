# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 15700 타일 채우기 4        | #
# ---------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    if N > M:
        N, M = M, N
    
    print(M // 2 * N + N // 2 * (M % 2))
