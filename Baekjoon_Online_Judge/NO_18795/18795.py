# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 18795 이동하기 3                   | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    print(sum(map(int, r_input().split())) + sum(map(int, r_input().split())))


if __name__ == "__main__":
    run()
