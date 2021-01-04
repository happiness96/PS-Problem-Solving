# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 2609 최대공약수와 최소 공배수        | #
# -------------------------------------- #


def get_gcd(n1, n2):
    rem = n1 % n2

    if rem == 0:
        return n2
    
    else:
        return get_gcd(n2, rem)


if __name__ == "__main__":
    num1, num2 = map(int, r_input().split())

    gcd = get_gcd(num1, num2)

    print(gcd)
    print((num1 * num2) // gcd)
