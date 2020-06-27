# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 27                   | #
# | 2902 KMP는 왜 KMP일까?    | #
# ---------------------------- #


if __name__ == "__main__":
    string = r_input().rstrip()

    for name in string.split('-'):
        print(name[0], end='')
