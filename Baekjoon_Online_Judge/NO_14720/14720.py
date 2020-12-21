# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 14720 우유 축제                     | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    store = list(map(int, r_input().split()))
    match = 0
    cnt = 0

    for val in store:
        if val == match:
            match = (match + 1) % 3
            cnt += 1
    
    print(cnt)
