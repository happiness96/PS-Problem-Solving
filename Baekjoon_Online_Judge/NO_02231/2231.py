# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 15                             | #
# | 2231 분해합                         | #
# -------------------------------------- #


def run():
    N = int(r_input())

    for num in range(1, N + 1):
        str_num = str(num)
        tot = num

        for s_n in str_num:
            tot += int(s_n)
        
        if tot == N:
            print(num)
            sys.exit()
        
    print(0)


if __name__ == "__main__":
    run()
