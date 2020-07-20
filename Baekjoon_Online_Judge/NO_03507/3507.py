# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 20                   | #
# | 3507 Automated Telephone Exchange| #
# ---------------------------- #


if __name__ == "__main__":
    n = int(r_input())
    cnt = 0

    for num1 in range(100):
        for num2 in range(100):
            if n - num1 - num2 == 0:
                cnt += 1
    
    print(cnt)
