# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 07                   | #
# | 9664 NASLJEDSTVO         | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    O = int(r_input())

    O *= N / (N - 1)
    
    flag = int(O % 1 == 0)
    O = int(O)

    print(O - flag, O)
