# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 01                   | #
# | 15645 내려가기 2          | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    max1 = max2 = max3 = 0
    min1 = min2 = min3 = 0

    for _ in range(N):
        num1, num2, num3 = map(int, r_input().split())

        min1 += min(num1, num2)
        min2 += min(num1, num2, num3)
        min3 += min(num2, num3)

        max1 += max(num1, num2)
        max2 += max(num1, num2, num3)
        max3 += max(num2, num3)
    
    print(min1, min2, min3)
    print(max1, max2, max3)