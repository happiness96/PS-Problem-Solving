# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 28                   | #
# | 2935 소음                 | #
# ---------------------------- #


if __name__ == "__main__":
    A = int(r_input())
    op = r_input().rstrip()
    B = int(r_input())

    if op == '+':
        print(A + B)
    
    else:
        print(A * B)
