# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 12981 공 포장하기                   | #
# -------------------------------------- #


if __name__ == "__main__":
    R, G, B = map(int, r_input().split())

    tot = R // 3 + G // 3 + B // 3

    R %= 3
    G %= 3
    B %= 3

    if [R, G, B].count(0) == 2:
        print(tot + 1)

    else:
        print(tot + max(R, G, B))
