# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 12                             | #
# | 19698 헛간 청약                     | #
# -------------------------------------- #


if __name__ == "__main__":
    N, W, H, L = map(int, r_input().split())

    print(min(N, (W // L) * (H // L)))
