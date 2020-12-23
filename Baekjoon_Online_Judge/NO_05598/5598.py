# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 23                             | #
# | 5598 카이사르 암호                  | #
# -------------------------------------- #


if __name__ == "__main__":
    before = r_input().rstrip()
    after = ''

    for ch in before:
        tmp = ord(ch) - 3

        if tmp < 65:
            tmp += 26
        
        after += chr(tmp)
    
    print(after)
