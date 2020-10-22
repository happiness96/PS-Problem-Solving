# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 22                             | #
# | 15721 번데기                          | #
# -------------------------------------- #


def run():
    A = int(r_input())
    T = int(r_input())
    S = int(r_input())

    cnt = [0, 0]
    step = 2
    turn = 0

    while True:
        round_start = [0, 1, 0, 1] + [0] * step + [1] * step

        for val in round_start:
            cnt[val] += 1

            if cnt[S] == T:
                print(turn)
                sys.exit()
            
            turn = (turn + 1) % A
        
        step += 1


if __name__ == "__main__":
    run()
