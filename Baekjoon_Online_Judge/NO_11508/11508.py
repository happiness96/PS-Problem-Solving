# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 01                   | #
# | 11508 2 + 1 세일          | #
# ---------------------------- #


def run():
    N = int(r_input())

    C = [int(r_input()) for _ in range(N)]
    C.sort(reverse=True)

    total = 0

    for ind, val in enumerate(C):
        if (ind + 1) % 3 == 0:
            continue
        
        total += val
    
    print(total)


if __name__ == "__main__":
    run()
