# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 3028 창영마을                       | #
# -------------------------------------- #


if __name__ == "__main__":
    order = r_input().rstrip()

    cup = [1, 0, 0]

    for o in order:
        if o == 'A':
            cup[0], cup[1] = cup[1], cup[0]
        
        elif o == 'B':
            cup[1], cup[2] = cup[2], cup[1]
        
        else:
            cup[0], cup[2] = cup[2], cup[0]

    print(cup.index(1) + 1)
