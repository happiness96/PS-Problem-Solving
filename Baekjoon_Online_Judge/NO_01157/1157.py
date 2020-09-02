# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 단어 공부                           | #
# -------------------------------------- #


if __name__ == "__main__":
    string = r_input().rstrip().upper()

    counting = {}

    for ch in string:
        if ch not in counting:
            counting[ch] = 0
        
        counting[ch] += 1

    max_val = 0
    res = ''

    for alpha, val in counting.items():
        if val > max_val:
            max_val = val
            res = alpha
        
        elif val == max_val:
            res = '?'

    print(res)
