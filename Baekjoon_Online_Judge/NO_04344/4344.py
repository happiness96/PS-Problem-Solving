# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 01                             | #
# | 평균은 넘겠지                      | #
# -------------------------------------- #


if __name__ == "__main__":
    C = int(r_input())

    for _ in range(C):
        N, *scores = map(int, r_input().split())
        avg = sum(scores) / N

        over_avg = 0

        for score in scores:
            if score > avg:
                over_avg += 1
        
        print('%.3f' % (over_avg / N * 100) + '%')
