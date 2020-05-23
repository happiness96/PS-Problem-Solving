# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 1934 최소공배수            | #
# ---------------------------- #


def get_gcd(num1, num2):

    mod = num2 % num1

    if mod == 0:
        return num1
    
    else:
        return get_gcd(mod, num1)


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        A, B = map(int, r_input().split())

        if A > B:
            A, B = B, A
        
        gcd = get_gcd(A, B)

        print(A // gcd * B)
