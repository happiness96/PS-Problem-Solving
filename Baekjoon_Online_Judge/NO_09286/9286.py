# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 9286 Gradabase                     | #
# -------------------------------------- #


def run():
    n = int(r_input())

    for t in range(1, n + 1):
        m = int(r_input())
        print('Case', str(t) + ':')

        for _ in range(m):
            g = int(r_input())

            if g < 6:
                print(g + 1)


if __name__ == "__main__":
    run()
