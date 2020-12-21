# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 3059 등장하지 않는 문자의 합        | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        S = r_input().rstrip()

        chk = [0] * 26
        result = 0

        for ch in set(S):
            chk[ord(ch) - 65] = 1
        
        for ind, val in enumerate(chk):
            if not val:
                result += 65 + ind
        
        print(result)
