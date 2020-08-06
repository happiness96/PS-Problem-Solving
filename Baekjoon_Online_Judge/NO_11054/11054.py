# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 28                   | #
# | 11054 가장 긴 바이토닉 부분 수열| #
# ---------------------------- #


def run():
    N = int(r_input())

    A = list(map(int, r_input().split()))

    result = 0
    maxi = max(A) + 1
    for i in range(N):
        left = [0] * maxi
        right = [0] * maxi
        
        for ind in range(i):
            left[A[ind]] = max(left[A[ind]], max(left[:A[ind]]) + 1)
        
        for ind in range(N - 1, i, -1):
            right[A[ind]] = max(right[A[ind]], max(right[:A[ind]]) + 1)
        print(i)
        print(left)
        print(right)
        result = max(result, max(left[:A[ind] + 1]) + max(right[:A[ind] + 1]) + 1)
    
    print(result)
    

if __name__ == "__main__":
    run()
