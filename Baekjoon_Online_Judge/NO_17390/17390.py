# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 17390 이건 꼭 풀어야 해!    | #
# ---------------------------- #


def run():
    N, Q = map(int, r_input().split())

    dp_B = [0]

    for val in sorted(map(int, r_input().split())):
        dp_B.append(dp_B[-1] + val)
    
    for _ in range(Q):
        L, R = map(int, r_input().split())
        print(dp_B[R] - dp_B[L - 1])
    

if __name__ == "__main__":
    run()
