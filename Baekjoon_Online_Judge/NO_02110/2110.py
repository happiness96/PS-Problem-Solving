# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 2110 공유기 설치           | #
# ---------------------------- #


if __name__ == "__main__":
    N, C = map(int, r_input().split())

    X = sorted([int(r_input()) for _ in range(N)])

    result = X[-1] - X[0]

    left = 0
    right = N - 1

    for _ in range(N - 2):
        mid = (right + left) // 2

        left_val = result[mid] - result[left]
        right_val = result[right] - result[mid]

        if left_val
