# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 18                             | #
# | 10156 과자                          | #
# -------------------------------------- #


if __name__ == "__main__":
    K, N, M = map(int, r_input().split())

    rem = M - K * N

    print(0 if rem >= 0 else -rem)
