# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 05                   | #
# | 14011 Small phD Restaurant| #
# ---------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    A = list(map(int, r_input().split()))
    B = list(map(int, r_input().split()))

    save = [[] for _ in range(1000001)]
