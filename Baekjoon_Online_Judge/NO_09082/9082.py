# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 9082 지뢰찾기                        | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        counting = list(map(int, list(r_input().rstrip())))
        bombs = list(r_input().rstrip())

        print((sum(counting) + 2) // 3)
