# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 9468 Islands in the Data Stream| #
# ---------------------------- #


if __name__ == "__main__":
    P = int(r_input())

    for _ in range(P):
        line = list(map(int, r_input().split()))
        cnt = 0
        stack = []

        for ind in range(1, 16):
            if not stack:
                if line[ind]:
                    stack.append(line[ind])
            
            else:
                while stack and stack[-1] > line[ind]:
                    stack.pop()
                    cnt += 1
                
                if stack and stack[-1] == line[ind]:
                    continue

                stack.append(line[ind])

        print(line[0], cnt)
