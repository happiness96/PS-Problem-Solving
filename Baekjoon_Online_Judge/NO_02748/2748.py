# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 30                             | #
# | 2748 피보나치 수 2                 | #
# -------------------------------------- #


if __name__ == "__main__":
    a, b = 0, 1
    N = int(r_input())

    for _ in range(N - 1):
        a, b = b, a + b
    
    print(b)
