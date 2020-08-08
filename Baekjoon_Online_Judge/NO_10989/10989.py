# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 08                             | #
# | 10989 수 정렬하기 3                | #
# -------------------------------------- #


def run():
    N = int(r_input())

    counting = [0] * 10001

    for _ in range(N):
        num = int(r_input())

        counting[num] += 1
    
    for num, count in enumerate(counting):
        if count:
            print('\n'.join([str(num)] * count))


if __name__ == "__main__":
    run()
