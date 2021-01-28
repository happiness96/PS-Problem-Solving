# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 25                             | #
# | 10816 숫자 카드 2                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    counter = {}

    for val in map(int, r_input().split()):
        counter[val] = counter.get(val, 0) + 1
    
    M = int(r_input())
    for val in map(int, r_input().split()):
        print(counter.get(val, 0), end=' ')
