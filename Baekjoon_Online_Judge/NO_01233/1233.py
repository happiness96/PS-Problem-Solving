# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 1233 주사위               | #
# ---------------------------- #


if __name__ == "__main__":
    S1, S2, S3 = map(int, r_input().split())

    save = [0] * (S1 + S2 + S3 + 1)

    for one in range(1, S1 + 1):
        for two in range(1, S2 + 1):
            for three in range(1, S3 + 1):
                save[one + two + three] += 1
    
    print(save.index(max(save)))
