# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 12                             | #
# | 3273 두 수의 합                     | #
# -------------------------------------- #


def run():
    n = int(r_input())
    arr = set(sorted(map(int, r_input().split())))
    x = int(r_input())
    res = 0

    for val in arr:
        if x - val in arr:
            res += 1
    
    print(res // 2)


if __name__ == "__main__":
    run()
