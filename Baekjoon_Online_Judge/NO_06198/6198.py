# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 15                             | #
# | 6198 옥상 정원 꾸미기               | #
# -------------------------------------- #


def run():
    N = int(r_input())

    height = [int(r_input()) for _ in range(N)]
    stack = []
    res = 0

    for h in height:
        if not stack:
            stack.append(h)
        
        else:
            while stack and stack[-1] <= h:
                stack.pop()
            
            res += len(stack)
            stack.append(h)

    print(res)


if __name__ == "__main__":
    run()
