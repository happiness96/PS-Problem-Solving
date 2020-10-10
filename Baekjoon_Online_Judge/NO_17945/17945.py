# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 17945 통학의 신                     | #
# -------------------------------------- #


if __name__ == "__main__":
    A, B = map(int, r_input().split())
    tmp = max(abs(A), abs(B)) * 2

    for num in range(-tmp, tmp + 1):
        if num ** 2 + 2 * A * num + B == 0:
            print(num, end=' ')
