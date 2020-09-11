# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 11                             | #
# | 1863 스카이라인 쉬운거              | #
# -------------------------------------- #


def run():
    n = int(r_input())

    stack = []
    res = 0

    for _ in range(n):
        x, y = map(int, r_input().split())

        if not stack:
            if y == 0:
                continue
            
            res += 1
            stack.append(y)
        
        else:
            if y > stack[-1]:
                res += 1
                stack.append(y)
            
            else:
                while stack and y < stack[-1]:
                    stack.pop()
                
                if y == 0 or stack and y == stack[-1]:
                    continue

                res += 1
                stack.append(y)
    
    print(res)


if __name__ == "__main__":
    run()
