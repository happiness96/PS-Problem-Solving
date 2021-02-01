# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 02                           | #
# | Day 01                             | #
# | 5397 키로거                         | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        left = deque()
        right = deque()

        for key in r_input().rstrip():
            if key == '<':
                if left:
                    right.appendleft(left.pop())
            
            elif key == '>':
                if right:
                    left.append(right.popleft())
            
            elif key == '-':
                if left:
                    left.pop()
            
            else:
                left.append(key)
        
        print(''.join(left + right))


if __name__ == "__main__":
    run()
