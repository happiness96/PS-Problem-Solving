# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 23                             | #
# | 1703 생장점                         | #
# -------------------------------------- #


if __name__ == "__main__":
    while True:
        a, *age = list(map(int, r_input().split()))

        if a == 0:
            break

        cnt = 1

        for ind in range(0, a * 2, 2):
            cnt *= age[ind]
            cnt -= age[ind + 1]
        
        print(cnt)
