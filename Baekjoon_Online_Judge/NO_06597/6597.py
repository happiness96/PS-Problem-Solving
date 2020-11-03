# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 01                             | #
# | 6597 트리 복구                      | #
# -------------------------------------- #


def tree_restore(pre_ord, in_ord):
    length = len(pre_ord)

    if length == 1:
        print(pre_ord[0], end='')
        return

    parent = pre_ord[0]
    par_ind = in_ord.index(parent)

    in_left = in_ord[: par_ind]
    in_right = in_ord[par_ind + 1:]

    len_left = len(in_left)
    len_right = length - len_left - 1

    pre_left = pre_ord[1: len_left + 1]
    pre_right = pre_ord[len_left + 1: ]

    if in_left:
        tree_restore(pre_left, in_left)
    
    if in_right:
        tree_restore(pre_right, in_right)
    
    print(parent, end='')


if __name__ == "__main__":
    for line in sys.stdin:
        pre_order, in_order = line.split()
        
        tree_restore(pre_order, in_order)
        print()
