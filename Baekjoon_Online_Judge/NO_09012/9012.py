# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 9012 괄호                 | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        PS = r_input().rstrip()

        stack = []
        result = 1

        for parenthesis in PS:
            if parenthesis == '(':
                stack.append(parenthesis)
            
            else:
                if not stack or stack[-1] == ')':
                    result = 0
                    break

                else:
                    stack.pop()
        
        if stack:
            result = 0
        
        print(['NO', 'YES'][result])