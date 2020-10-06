# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19946 2의 제곱수 계산하기             | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    print(bin(N).count('1'))
