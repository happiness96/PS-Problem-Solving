# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 01                   | #
# | 11785 Programming Contest Strategy| #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for testcase in range(1, T + 1):
        N, L = map(int, r_input().split())
        time = sorted(map(int, r_input().split()))

        total = 0
        acc = 0
        solved = 0

        print("Case " + str(testcase), end=': ')

        for val in time:
            total += val

            if total > L:
                total -= val
                break
            
            solved += 1
            acc += total

        print(solved, total, acc)
