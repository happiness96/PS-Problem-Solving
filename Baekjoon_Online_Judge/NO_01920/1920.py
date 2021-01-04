# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 1920 수 찾기                        | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    A = list(map(int, r_input().split()))

    M = int(r_input())
    B = list(map(int, r_input().split()))

    A.sort()

    for b in B:
        left = 0
        right = N - 1
        
        while True:
            if right - left <= 1:
                if A[left] == b or A[right] == b:
                    print(1)
                
                else:
                    print(0)
                break
            
            mid = (left + right) // 2

            if A[mid] >= b:
                right = mid
            
            else:
                left = mid
