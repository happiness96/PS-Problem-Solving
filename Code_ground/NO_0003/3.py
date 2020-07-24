# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 24                   | #
# | 시험 공부                  | #
# ---------------------------- #


def run():
    T = int(r_input())

    for testcase in range(1, T + 1):
        N, K = map(int, r_input().split())

        scores = list(map(int, r_input().split()))

        scores.sort()

        total = 0
        
        for ind in range(1, K + 1):
            total += scores[-ind]
        
        print('Case #' + str(testcase))
        print(total)


if __name__ == "__main__":
    run()
