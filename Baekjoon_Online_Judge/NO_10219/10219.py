# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 10                             | #
# | 10219 Meats On The Grill           | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        H, W = map(int, r_input().split())

        for _ in range(H):
            print(r_input().rstrip()[::-1])
