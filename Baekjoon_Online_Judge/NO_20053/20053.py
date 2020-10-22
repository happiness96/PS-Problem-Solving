# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 22                             | #
# | 20053 최소, 최대 2                  | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        arr = list(map(int, r_input().split()))

        print(min(arr), max(arr))


if __name__ == "__main__":
    run()
