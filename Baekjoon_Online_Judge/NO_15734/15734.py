# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 15734 명장 남정훈                   | #
# -------------------------------------- #


if __name__ == "__main__":
    L, R, A = map(int, r_input().split())

    if L == R:
        print((L + A // 2) * 2)
    
    elif L > R:
        rem = L - R

        if rem > A:
            R += A
            print(R * 2)
        
        else:
            A -= rem
            print((L + A // 2) * 2)
    
    else:
        rem = R - L

        if rem > A:
            L += A
            print(L * 2)
        
        else:
            A -= rem
            print((R + A // 2) * 2)
