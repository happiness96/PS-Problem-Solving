# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 25                             | #
# | 4779 칸토어 집합                    | #
# -------------------------------------- #


def devide(start_loc, end_loc, length):
    if length == 1:
        return
    
    K = (end_loc - start_loc) // 3
    first = start_loc + K
    second = start_loc + K * 2

    for i in range(first, second):
        string[i] = ' '

    devide(start_loc, first, length // 3)
    devide(second, end_loc, length // 3)


if __name__ == "__main__":
    for N in sys.stdin:
        N = int(N)
        total_length = 3 ** N

        string = list('-' * total_length)

        devide(0, total_length, total_length)

        print(''.join(string))
