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
    first_son, first_mother = map(int, r_input().split())
    second_son, second_mother = map(int, r_input().split())
    
    if first_mother > second_mother:
        first_mother, second_mother = second_mother, first_mother
        first_son, second_son = second_son, first_son

    gcd_mother = get_gcd(first_mother, second_mother)
    result_mother = first_mother // gcd_mother * second_mother
    result_son = first_son * (result_mother // first_mother) + second_son * (result_mother // second_mother)

    flag = 0

    if result_son > result_mother:
        flag = 1
        result_mother, result_son = result_son, result_mother
    
    result_gcd = get_gcd(result_son, result_mother)

    if flag:
        result_mother, result_son = result_son, result_mother
    
    print(result_son // result_gcd, result_mother // result_gcd)
