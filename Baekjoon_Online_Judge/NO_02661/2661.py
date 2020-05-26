# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 26                   | #
# | 2661 좋은 수열            | #
# ---------------------------- #


def dfs(number):
    length = len(number)

    tmp = ''

    for i in range(1, length // 2 + 1):
        tmp = number[length - i] + tmp
        cmp = number[length - 2 * i:length - i]
        
        if tmp == cmp:
            return
    
    if length == N:
        print(number)
        sys.exit()
    
    else:
        dfs(number + '1')
        dfs(number + '2')
        dfs(number + '3')


if __name__ == "__main__":
    N = int(r_input())

    dfs('')
