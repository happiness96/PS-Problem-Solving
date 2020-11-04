# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 05                             | #
# | 13268 셔틀런                        | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    loc = 0

    while N:
        for run in [5, 10, 15, 20]:
            if N >= run:
                N -= run
                loc += run
            
            else:
                loc += N
                print((loc + 4) // 5)
                sys.exit()
            
            if N >= run:
                N -= run
                loc -= run
            
            else:
                loc -= N
                print((loc + 4) // 5)
                sys.exit()
    print(0)
