# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 27                   | #
# | 16431 베시와 데이지        | #
# ---------------------------- #


if __name__ == "__main__":
    bessie_row, bessie_col = map(int, r_input().split())
    daisy_row, daisy_col = map(int, r_input().split())
    john_row, john_col = map(int, r_input().split())

    b_distance = abs(bessie_row - john_row) + abs(bessie_col - john_col)
    d_distance = abs(daisy_row - john_row) + abs(daisy_col - john_col)

    b_distance -= min(abs(bessie_row - john_row), abs(bessie_col - john_col))

    print('bessie' if b_distance < d_distance else 'daisy' if b_distance > d_distance else 'tie')
