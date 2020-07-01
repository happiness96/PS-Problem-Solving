# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 01                   | #
# | 12894 Equivalent Strings| #
# ---------------------------- #


def get_result(string):
    len_s = len(string)

    if len_s % 2:
        return string
    
    str1 = get_result(string[:len_s // 2])
    str2 = get_result(string[len_s // 2:])

    return str1 + str2 if str1 < str2 else str2 + str1


if __name__ == "__main__":
    a = r_input().rstrip()
    b = r_input().rstrip()

    print(['NO', 'YES'][get_result(a) == get_result(b)])
