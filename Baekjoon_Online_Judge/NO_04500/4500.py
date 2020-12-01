# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 4500 “Bubble Gum, Bubble Gum, in the dish, how many pieces do you wish?”| #
# -------------------------------------- #


def run():
    t = int(r_input())

    for _ in range(t):
        names = list(map(str, r_input().rstrip().split()))

        first_name = r_input().rstrip()
        ind = names.index(first_name)

        length = len(names)

        n = int(r_input()) - 1

        ind += n
        ind %= length
        
        print(names[ind])


if __name__ == "__main__":
    run()
