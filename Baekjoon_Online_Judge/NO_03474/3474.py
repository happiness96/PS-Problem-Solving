# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 07                             | #
# | 3474 교수가 된 현우                 | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        step = 1
        tot = 0

        while True:
            tmp = 5 ** step

            if tmp > N:
                break

            tot += N // tmp
            step += 1
        
        print(tot)


if __name__ == "__main__":
    run()
