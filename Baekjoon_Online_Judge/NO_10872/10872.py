# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 10872 팩토리얼                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    result = 1

    for number in range(1, N + 1):
        result *= number
    
    print(result)
