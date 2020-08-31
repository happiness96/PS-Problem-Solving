# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 31                             | #
# | 시험 성적                          | #
# -------------------------------------- #


if __name__ == "__main__":
    score = int(r_input())

    print('A' if 90 <= score <= 100 else 'B' if 80 <= score else 'C' if 70 <= score else 'D' if 60 <= score else 'F')
