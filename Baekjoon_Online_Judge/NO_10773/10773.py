# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 10773 제로                | #
# ---------------------------- #


def run():
    K = int(r_input())

    stack = []

    for _ in range(K):
        number = int(r_input())

        if number:
            stack.append(number)
        
        else:
            stack.pop()
    
    print(sum(stack))


if __name__ == "__main__":
    run()
