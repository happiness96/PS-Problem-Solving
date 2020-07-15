# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 2012 등수 매기기          | #
# ---------------------------- #


def run():
    N = int(r_input())

    result = 0

    predict_rank = [0] + [int(r_input()) for _ in range(N)]
    predict_rank.sort()

    for rank in range(1, N + 1):
        result += abs(rank - predict_rank[rank])
    
    print(result)


if __name__ == "__main__":
    run()
