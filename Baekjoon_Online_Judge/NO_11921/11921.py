# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 06                             | #
# | 11921 0.1                          | #
# -------------------------------------- #


def run():
    r_input()

    save = [int(r_input()) for _ in range(110000)]
    
    print('\n'.join(['110000', str(sum(save))]))


if __name__ == "__main__":
    run()
