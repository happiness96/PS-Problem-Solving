# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 18268 Cow Gymnastics               | #
# -------------------------------------- #


def run():
    K, N = map(int, r_input().split())

    better_than = [[1] * (N + 1) for _ in range(N + 1)]

    for _ in range(N):
        ranking = list(map(int, r_input().split()))

        for rank, number1 in enumerate(ranking):
            for number2 in ranking[rank + 1:]:
                better_than[number2][number1] = 0

    total = 0
    for i in range(1, N + 1):
        total += sum(better_than[i][1:])

    print(total - N)


if __name__ == "__main__":
    run()
