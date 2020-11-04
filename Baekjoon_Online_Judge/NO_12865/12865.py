# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 04                             | #
# | 12865 평범한 배낭                   | #
# -------------------------------------- #


def run():
    N, K = map(int, r_input().split())

    save = [0] * (K + 1)

    for _ in range(N):
        W, V = map(int, r_input().split())

        for weight in range(K - W, -1, -1):
            if save[weight]:
                a_weight = weight + W
                save[a_weight] = max(save[a_weight], save[weight] + V)

        if W <= K:
            save[W] = max(save[W], V)

    print(max(save))


if __name__ == "__main__":
    run()
