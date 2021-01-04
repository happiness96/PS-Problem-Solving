# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 20528 끝말잇기                      | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    flag = 1
    words = list(map(str, r_input().rstrip().split()))
    chk = words[0][0]

    for word in words:
        if word[0] != chk:
            flag = 0
            break
    
    print(flag)
