# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 29                             | #
# | 15501 부당한 퍼즐                   | #
# -------------------------------------- #


if __name__ == "__main__":
    n = int(r_input())

    first = list(map(int, r_input().rstrip().split()))
    second = list(map(int, r_input().rstrip().split()))
    
    ind = second.index(first[0])
    
    if first in [second[ind:] + second[:ind], second[:ind + 1][::-1] + second[ind + 1:][::-1]]:
        print('good puzzle')
    
    else:
        print('bad puzzle')
