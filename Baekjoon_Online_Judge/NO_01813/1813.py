# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 14                             | #
# | 1813 마지막 한마디                  | #
# -------------------------------------- #


def run():
    N = int(r_input())

    is_it_true = {}

    for val in map(int, r_input().split()):
        is_it_true[val] = is_it_true.get(val, 0) + 1;
    
    for value in sorted(is_it_true.keys(), reverse=True):
        if is_it_true[value] == value:
            print(value)
            sys.exit()

    if 0 not in is_it_true:
        print(0)
    
    else:
        print(-1)


if __name__ == "__main__":
    run()
