# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19951 태상이의 훊련소 생활            | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())
    heights = list(map(int, r_input().split()))

    order = [0] * (N + 2)

    for _ in range(M):
        a, b, k = map(int, r_input().split())
        order[a] += k
        order[b + 1] -= k

    acc = 0
    for ind in range(1, N + 1):
        acc += order[ind]

        heights[ind  - 1] += acc
    
    print(*heights)


if __name__ == "__main__":
    run()
