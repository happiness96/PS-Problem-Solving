# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 11                             | #
# | 6236 용돈 관리                      | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    save = [int(r_input()) for _ in range(N)]

    l = max(save)
    r = sum(save)

    while True:
        mid = (l + r) // 2

        K = 0
        rem = 0

        for cost in save:
            if cost > rem:
                rem = mid
                K += 1
            
            rem -= cost

        if r - l <= 1:
            if K > M:
                print(r)
            else:
                print(l)
            break
        
        if K > M:
            l = mid
        
        else:
            r = mid


if __name__ == "__main__":
    run()
