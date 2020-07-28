# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 28                   | #
# | 11256 사탕                | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        J, N = map(int, r_input().split())

        save = []

        for _ in range(N):
            R, C = map(int, r_input().split())
            save.append(R * C)
        
        save.sort()

        for ind, val in enumerate(save[::-1]):
            J -= val

            if J <= 0:
                print(ind + 1)
                break


if __name__ == "__main__":
    run()
