# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 11                             | #
# | 6996 에너그램                       | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        A, B = map(str, r_input().split())

        if sorted(A) == sorted(B):
            print(A + ' & ' + B + ' are anagrams.')
        
        else:
            print(A + ' & ' + B + ' are NOT anagrams.')
