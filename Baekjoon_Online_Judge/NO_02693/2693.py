# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 2693 N번째 큰 수           | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        print(sorted(map(int, r_input().split()))[-3])
