# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 1735 분수 합              | #
# ---------------------------- #


def get_gcd(number1, number2):
    mod = number2 % number1
    
    if mod == 0:
        return number1

    else:
        return get_gcd(mod, number1)


if __name__ == "__main__":
    first_son, first_mother = map(int, r_input().rstrip().split())
    second_son, second_mother = map(int, r_input().rstrip().split())

    result_son = first_son * second_mother + second_son * first_mother
    result_mother = first_mother * second_mother

    gcd = get_gcd(result_son, result_mother)

    print(result_son // gcd, result_mother // gcd)
