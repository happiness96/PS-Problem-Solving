# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 27                   | #
# | 1806 부분합               | #
# ---------------------------- #


def run():
    INF = sys.maxsize

    N, S = map(int, r_input().split())
    arr = list(map(int, r_input().split()))

    i = 0

    result = INF
    tot = 0

    for j in range(N):
        tot += arr[j]

        while tot >= S:
            result = min(result, j - i + 1)
            tot -= arr[i]
            i += 1
        
    print(0 if result == INF else result)


if __name__ == "__main__":
    run()
