# -*- encoding: utf-8 -*-
import sys
import bisect
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 14170 Counting Haybales  | #
# ---------------------------- #


def run():
    N, Q = map(int, r_input().split())
    locations = sorted(map(int, r_input().split()))

    for _ in range(Q):
        A, B = map(int, r_input().split())

        left_a = bisect.bisect_left(locations, A)
        right_b = bisect.bisect_right(locations, B)
        
        print(right_b - left_a)


if __name__ == "__main__":
    run()
