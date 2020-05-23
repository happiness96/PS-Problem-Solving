# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 10453 문자열 변환          | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        string_a, string_b = map(str, r_input().rstrip().split())

        stack_A = []
        stack_B = []

        for ind in range(len(string_a)):
            if string_a[ind] == 'a':
                stack_A.append(ind)
            
            if string_b[ind] == 'a':
                stack_B.append(ind)

        cnt = 0

        for ind, val in enumerate(stack_A):
            cnt += abs(val - stack_B[ind])
        
        print(cnt)


if __name__ == "__main__":
    run()
