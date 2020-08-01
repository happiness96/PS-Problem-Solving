# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 10987 모음의 개수          | #
# ---------------------------- #


if __name__ == "__main__":
    word = r_input().rstrip()
    res = 0

    for ch in word:
        if ch in 'aeiou':
            res += 1

    print(res)
