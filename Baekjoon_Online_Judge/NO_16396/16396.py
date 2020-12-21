# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 16396 선 그리기                     | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    line = [0] * 10001

    for _ in range(N):
        x, y = map(int, r_input().split())

        for ind in range(x, y):
            line[ind] = 1
    
    print(sum(line))
