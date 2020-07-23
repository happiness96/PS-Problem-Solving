# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 2670 연속부분최대곱         | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    save = [float(r_input()) for _ in range(N)]

    result = 0
    tmp = 1

    for val in save:
        tmp *= val

        tmp = max(tmp, val)
        result = max(result, tmp)
    
    print('%.3f' % result)
