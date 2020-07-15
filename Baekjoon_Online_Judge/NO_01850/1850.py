# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 1850 최대공약수            | #
# ---------------------------- #


def get_gcd(num1, num2):
    mod = num2 % num1

    if mod == 0:
        return num1
    
    else:
        return get_gcd(mod, num1)


if __name__ == "__main__":
    A, B = map(int, r_input().split())

    if A > B:
        A, B = B, A

    print('1' * get_gcd(A, B))
