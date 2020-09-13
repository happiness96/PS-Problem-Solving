# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 13                             | #
# | 10815 숫자 카드                     | #
# -------------------------------------- #


def run():
    N = int(r_input())
    A = set(map(int, r_input().split()))

    M = int(r_input())
    B = list(map(int, r_input().split()))

    for b in B:
        print(int(b in A), end=' ')


if __name__ == "__main__":
    run()
