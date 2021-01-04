# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 20492 세금                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    
    print(int(N * 0.78), int(N * 0.8 + (N - N * 0.8) * 0.78))
