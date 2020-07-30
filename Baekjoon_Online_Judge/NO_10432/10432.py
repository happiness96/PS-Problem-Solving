# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 30                   | #
# | 10432 데이터 스트림의 섬    | #
# ---------------------------- #


if __name__ == "__main__":
    P = int(r_input())

    for _ in range(P):
        data = list(map(int, r_input().split()))

        stack = []
        res = 0

        for val in data[1:]:
            while stack and stack[-1] > val:
                stack.pop()
                res += 1
            
            if val:
                if not stack or val != stack[-1]:
                    stack.append(val)
            
        print(data[0], res)
