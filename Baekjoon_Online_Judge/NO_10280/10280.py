# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 14                   | #
# | 10280 Pizza voting       | #
# ---------------------------- #


if __name__ == "__main__":
    n, p = map(int, r_input().split())
    
    start = n // 3 + 1
    end = start + (n - 1) // 3

    print('YES' if start <= p <= end else 'NO')
