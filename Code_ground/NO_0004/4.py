# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 24                   | #
# | 다트 게임                  | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for testcase in range(1, T + 1):
        A, B, C, D, E = map(int, r_input().split())

        N = int(r_input())
        total = 0

        for _ in range(N):
            x, y = map(int, r_input().split())