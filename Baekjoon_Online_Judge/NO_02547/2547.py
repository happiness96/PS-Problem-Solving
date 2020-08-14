# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 14                             | #
# | 2547 사탕 선생 고창영               | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        r_input()

        N = int(r_input())
        total = 0

        for _ in range(N):
            total += int(r_input())

        print(['YES', 'NO'][bool(total % N)])


if __name__ == "__main__":
    run()
