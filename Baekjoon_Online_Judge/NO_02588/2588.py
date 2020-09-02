# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 곱셈                               | #
# -------------------------------------- #


if __name__ == "__main__":
    num1 = int(r_input())
    num2 = r_input().rstrip()

    for mult in num2[::-1]:
        print(num1 * int(mult))
    
    print(num1 * int(num2))
