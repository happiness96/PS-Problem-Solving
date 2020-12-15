# -*- encoding: utf-8 -*-
import sys
from itertools import permutations
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 5568 카드 놓기                      | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())
    k = int(r_input())

    numbers = []

    for _ in range(n):
        number = r_input().rstrip()
        numbers.append(number)
    
    result = set()
    
    for case in permutations(numbers, k):
        result.add(''.join(case))
    
    print(len(result))
