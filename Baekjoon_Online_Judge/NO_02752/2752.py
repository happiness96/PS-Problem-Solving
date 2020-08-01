# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 2752 세수정렬              | #
# ---------------------------- #


if __name__ == "__main__":
    l = list(map(int, r_input().split()))

    print(*sorted(l))
