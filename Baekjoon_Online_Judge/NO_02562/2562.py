# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 01                             | #
# | 최댓값                             | #
# -------------------------------------- #


if __name__ == "__main__":
    result = 0
    result_ind = 0

    for ind in range(1, 10):
        number = int(r_input())

        if number > result:
            result = number
            result_ind = ind

    print(result)
    print(result_ind)
