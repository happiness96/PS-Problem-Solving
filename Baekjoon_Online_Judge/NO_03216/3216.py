# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 17                             | #
# | 3216 다운로드                       | #
# -------------------------------------- #


def run():
    N = int(r_input())

    tot_D = 0
    tot_V = 0
    last = 0

    for _ in range(N):
        D, V = map(int, r_input().split())

        tot_V += V
        tmp = tot_V - tot_D
        last = max(tmp, last)
        tot_D += D
    
    print(last)


if __name__ == "__main__":
    run()
