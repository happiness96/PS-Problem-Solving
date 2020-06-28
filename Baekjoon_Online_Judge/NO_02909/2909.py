# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 28                   | #
# | 2909 캔디 구매            | #
# ---------------------------- #


if __name__ == "__main__":
    C, K = map(int, r_input().split())

    div, mod = divmod(C, 10 ** K)

    if mod >= 5 * 10 ** (K - 1):
        print((div + 1) * 10 ** K)
    
    else:
        print(div * 10 ** K)
