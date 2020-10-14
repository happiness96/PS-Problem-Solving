# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 6609 모기곱셈                      | #
# -------------------------------------- #


def run():
    for line in sys.stdin:
        M, P, L, E, R, S, N = map(int, line.split())
        
        for _ in range(N):
            M, P, L = P // S, L // R, M * E
        
        print(M)


if __name__ == "__main__":
    run()
