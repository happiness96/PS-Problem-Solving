# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 06                             | #
# | 9084 동전                          | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        coins = list(map(int, r_input().split()))
        cost = int(r_input())

        save = [0] * (cost + 1)

        for coin in coins:
            if coin <= cost:
                save[coin] += 1

            for ind, val in enumerate(save):
                tmp = ind + coin

                if tmp <= cost:
                    save[tmp] += save[ind]
        
        print(save[-1])


if __name__ == "__main__":
    run()
