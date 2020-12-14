# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 14                             | #
# | 2966 찍기                          | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    answer = r_input().rstrip()

    A = 0
    A_ans = ['A', 'B', 'C']
    B = 0
    B_ans = ['B', 'A', 'B', 'C']
    C = 0
    C_ans = ['C', 'C', 'A', 'A', 'B', 'B']

    for ind, ans in enumerate(answer):
        if ans == A_ans[ind % 3]:
            A += 1
        
        if ans == B_ans[ind % 4]:
            B += 1
        
        if ans == C_ans[ind % 6]:
            C += 1
    
    max_score = max(A, B, C)

    print(max_score)

    if A == max_score:
        print('Adrian')
    
    if B == max_score:
        print('Bruno')
    
    if C == max_score:
        print('Goran')
