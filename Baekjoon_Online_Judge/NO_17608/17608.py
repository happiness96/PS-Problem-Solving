# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 25                   | #
# | 17608 막대기              | #
# ---------------------------- #


def run():
    N = int(r_input())

    cur_height = 0
    result = 0

    for height in [int(r_input()) for _ in range(N)][::-1]:
        if height > cur_height:
            cur_height = height
            result += 1
    
    print(result)


if __name__ == "__main__":
    run()
