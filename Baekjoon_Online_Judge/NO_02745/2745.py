# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 2745 진법 변환                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N, B = map(str, r_input().rstrip().split())
    N = N[::-1]
    B = int(B)

    result = 0

    for ind, ch in enumerate(N):
        if 'A' <= ch <= 'Z':
            ch = ord(ch) - 55

        else:
            ch = int(ch)
        
        result += ch * B ** ind
    
    print(result)
