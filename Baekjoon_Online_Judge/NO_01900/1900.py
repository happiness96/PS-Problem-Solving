# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 1900 레슬러                         | #
# -------------------------------------- #


def run():
    N = int(r_input())

    save = []

    for ind in range(1, N + 1):
        p, mp = map(int, r_input().split())

        save.append(((mp - 1) / p, ind))
    
    save.sort(reverse=True)
    
    for _, res in save:
        print(res)


if __name__ == "__main__":
    run()
