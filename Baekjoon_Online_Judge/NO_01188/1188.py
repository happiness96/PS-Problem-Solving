# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 18                             | #
# | 1188 음식 평론가                    | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    flag = 0

    for num in range(1, M + 1):
        if (N / M * num ) % 1 == 0:
            flag = num
            break
    
    print(M - M // flag)
