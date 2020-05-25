# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 25                   | #
# | 17608 막대기              | #
# ---------------------------- #


def run():
    N = int(r_input())

    stack = []

    for _ in range(N):
        height = int(r_input())

        if not stack:
            stack.append(height)
        
        else:
            while True:
                if not stack:
                    stack.append(height)
                    break
                
                if stack[-1] < height:
                    stack.pop()
                    
                elif stack[-1] == height:
                    break
            
                else:
                    stack.append(height)
    
    print(len(stack))


if __name__ == "__main__":
    run()
