# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 1946 신입 사원             | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        save = [0] * (N + 1)

        for _ in range(N):
            A, B = map(int, r_input().split())
            save[A] = B
        print(save)

    
if __name__ == "__main__":
    run()
