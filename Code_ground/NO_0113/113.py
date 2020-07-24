# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 24                   | #
# | 1비트 개수 세기            | #
# ---------------------------- #


def run():
    T = int(r_input())

    for testcase in range(1, T + 1):
        N = int(r_input())

        print('Case #' + str(testcase))
        print(bin(N).count('1'))


if __name__ == "__main__":
    run()
