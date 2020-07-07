# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 07                   | #
# | 11908 카드                | #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())
    c = list(map(int, r_input().split()))

    print(sum(c) - max(c))
