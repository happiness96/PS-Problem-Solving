# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 17299 오등큰수                      | #
# -------------------------------------- #


def run():
    N = int(r_input())

    number_count = {}
    res = ['-1'] * N
    A = list(map(int, r_input().split()))

    for val in A:
        number_count[val] = number_count.get(val, 0) + 1
    
    stack = []
    
    for ind, val in enumerate(A):
        tmp = number_count[val]

        while True:
            if not stack:
                stack.append((tmp, ind, val))
                break
            
            elif stack[-1][0] < tmp:
                t, i, v = stack.pop()
                res[i] = str(val)
            
            else:
                stack.append((tmp, ind, val))
                break
    
    print(' '.join(res))


if __name__ == "__main__":
    run()
