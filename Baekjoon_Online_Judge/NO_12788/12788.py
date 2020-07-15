# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 12788 제 2회 IUPC는 잘 개최될 수 있을까?| #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    M, P = map(int, r_input().split())
    need = M * P

    A = sorted(map(int, r_input().split()), reverse=True)
    
    for ind, val in enumerate(A):
        need -= val

        if need <= 0:
            print(ind + 1)
            sys.exit()
    
    print("STRESS")
