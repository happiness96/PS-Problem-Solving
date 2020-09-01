# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 01                             | #
# | 더하기 사이클                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    ori = N

    cycle_length = 0

    while True:
        cycle_length += 1

        N = N % 10 * 10 + (N % 10 + N // 10) % 10

        if N == ori:
            break
    
    print(cycle_length)
