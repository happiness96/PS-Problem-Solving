# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 11                             | #
# | 15815 천재 수학자 성필              | #
# -------------------------------------- #


if __name__ == "__main__":
    string = r_input().rstrip()

    stack = []

    for ch in string:
        if ch == '*':
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num2 * num1)
        
        elif ch == '/':
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num2 // num1)
        
        elif ch == '+':
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num2 + num1)
        
        elif ch == '-':
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num2 - num1)
        
        else:
            stack.append(int(ch))
    
    print(stack[0])
