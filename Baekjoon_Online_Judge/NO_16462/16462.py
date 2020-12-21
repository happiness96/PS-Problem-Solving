# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 16462 '나교수' 교수님의 악필        | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    total = 0
    
    for _ in range(N):
        Q = list(r_input().rstrip())

        for ind, val in enumerate(Q):
            if val in '06':
                Q[ind] = '9'

        total += min(int(''.join(Q)), 100)
    
    result = total / N

    if result % 1 >= 0.5:
        result += 1
    
    print(int(result))
