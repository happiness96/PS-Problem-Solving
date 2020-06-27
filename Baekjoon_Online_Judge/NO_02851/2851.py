# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 2851 슈퍼 마리오           | #
# ---------------------------- #


if __name__ == "__main__":
    total = 0
    result = 0

    for _ in range(10):
        total += int(r_input())

        if abs(100 - total) <= abs(100 - result):
            result = total
        
    print(result)
