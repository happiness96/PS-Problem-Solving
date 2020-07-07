# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 07                   | #
# | 1817 좋은 자동차 번호판     | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    for _ in range(N):
        alpha, number = r_input().rstrip().split('-')
        alpha_value = 0

        for ind, ch in enumerate(alpha):
            alpha_value += (ord(ch) - 65) * 26 ** (2 - ind)
        
        if abs(alpha_value - int(number)) <= 100:
            print('nice')
        
        else:
            print('not nice')
