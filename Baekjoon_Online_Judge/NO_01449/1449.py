# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 1449 수리공 항승           | #
# ---------------------------- #


def run():
    N, L = map(int, r_input().split())

    locations = sorted(map(int, r_input().split()))

    cnt = 0

    start = 0

    for loc in locations:
        if not start:
            start = loc
        
        else:
            if loc - start >= L:
                cnt += 1
                start = loc
    
    print(cnt + 1)


if __name__ == "__main__":
    run()
