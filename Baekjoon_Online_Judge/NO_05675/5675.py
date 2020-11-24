# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 5675 시침과 분침                    | #
# -------------------------------------- #


if __name__ == "__main__":
    for angle in sys.stdin:
        print('NY'[int(angle) % 6 == 0])
