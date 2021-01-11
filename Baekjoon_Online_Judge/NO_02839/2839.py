# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 11                             | #
# | 2839 설탕 배달                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    start = N - N % 5

    for five in range(start, -1, -5):
        rem = N - five

        if rem % 3 == 0:
            print(rem // 3 + five // 5)
            sys.exit()
    
    print(-1)
