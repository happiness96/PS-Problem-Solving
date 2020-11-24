# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 8320 직사각형을 만드는 방법         | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())
    save = [0] * (n + 1)

    for num in range(2, n + 1):
        for chk in range(num * 2, min(n + 1, num ** 2 + 1), num):
            save[chk] += 1
    
    print(sum(save) + n)
