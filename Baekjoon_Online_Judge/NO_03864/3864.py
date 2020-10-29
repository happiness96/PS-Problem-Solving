# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 29                             | #
# | 3864 행복한 전화 통화               | #
# -------------------------------------- #


def run():
    while True:
        N, M = map(int, r_input().split())

        if N == M == 0:
            break

        calling = []

        for _ in range(N):
            source, destination, start, duration = map(int, r_input().split())

            calling.append((start, start + duration))

        calling.sort()

        for _ in range(M):
            start, duration = map(int, r_input().split())
            end = start + duration

            res = 0

            for call_st, call_end in calling:
                if call_st >= end:
                    break

                if call_end > start:
                    res += 1
            
            print(res)


if __name__ == "__main__":
    run()
