# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 08                             | #
# | 11899 괄호 끼워넣기                 | #
# -------------------------------------- #


if __name__ == "__main__":
    string = r_input().rstrip()

    stack = []

    for bracket in string:
        if bracket == '(':
            stack.append(bracket)
        
        else:
            if not stack or stack[-1] != '(':
                stack.append(bracket)

            else:
                stack.pop()
    
    print(len(stack))
