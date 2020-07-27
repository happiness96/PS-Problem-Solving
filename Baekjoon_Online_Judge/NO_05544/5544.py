# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 27                   | #
# | 5544 심부름 가는 길        | #
# ---------------------------- #


if __name__ == "__main__":
    total_min = 0
    total_sec = 0

    for _ in range(4):
        time = int(r_input())
        total_sec += time

    total_min += total_sec // 60
    total_sec %= 60

    print(total_min)
    print(total_sec)
