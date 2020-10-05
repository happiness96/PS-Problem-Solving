# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 30                             | #
# | 15885 고장난 시계                  | #
# -------------------------------------- #


if __name__ == "__main__":
    a, b = map(int, r_input().split())
    
    print(int(abs(a / b - 1) * 2))
