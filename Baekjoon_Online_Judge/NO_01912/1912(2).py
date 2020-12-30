# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 30                             | #
# | 1912 연속합                        | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    numbers = list(map(int, r_input().split()))

    dp = [-1001]

    for number in numbers:
        dp.append(max(dp[-1] + number, number))
    
    print(max(dp))
