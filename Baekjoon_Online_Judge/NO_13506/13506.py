# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 12                             | #
# | 13506 카멜레온 부분 문자열           | #
# -------------------------------------- #


def run():
    S = r_input().rstrip()
    length = len(S)

    if length < 3:
        print(-1)
        sys.exit()
    
    length -= 1
    pi = [0] * length
    i = 0
    j = 1
    maxi = 0

    while j < length:
        if S[i] == S[j]:
            i += 1
            pi[j] = i
            j += 1
            maxi = max(maxi, i)
        
        elif i == 0:
            j += 1
        
        else:
            i = pi[i - 1]
    
    for ind in range(maxi, 0, -1):
        sub_str = S[:ind]
        
        if S.endswith(sub_str):
            print(sub_str)
            sys.exit()
    
    print(-1)


if __name__ == "__main__":
    run()
