# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 5585 거스름돈                       | #
# -------------------------------------- #


if __name__ == "__main__":
    pay = int(r_input())
    rem = 1000 - pay

    papers = [500, 100, 50, 10, 5, 1]
    result = 0

    for paper in papers:
        result += rem // paper
        rem %= paper
    
    print(result)
