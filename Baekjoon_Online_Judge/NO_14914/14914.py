# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 28                   | #
# | 14914 사과와 바나나 나눠주기 | #
# ---------------------------- #


if __name__ == "__main__":
    a, b = map(int, r_input().split())

    for cnt in range(1, min(a, b) + 1):
        if a % cnt == b % cnt == 0:
            print(cnt, a // cnt, b // cnt)
