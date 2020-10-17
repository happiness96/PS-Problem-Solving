# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 17                             | #
# | 17298 오큰수                       | #
# -------------------------------------- #


def run():
    N = int(r_input())
    stack = []
    res = ['-1'] * N

    for ind, A in enumerate(map(int, r_input().split())):
        while True:
            if not stack:
                stack.append((A, ind))
                break

            elif stack[-1][0] < A:
                _, pop_ind = stack.pop()
                res[pop_ind] = str(A)

            else:
                stack.append((A, ind))
                break
    print(' '.join(res))


if __name__ == "__main__":
    run()
