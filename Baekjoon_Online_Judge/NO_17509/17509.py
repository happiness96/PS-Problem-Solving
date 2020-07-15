# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 17509 And the Winner is... Ourselves!| #
# ---------------------------- #


if __name__ == "__main__":
    total = 0

    save = []

    for ind in range(11):
        D, V = map(int, r_input().split())
        save.append(D)
        total += 20 * V
    
    acc = 0
    for minutes in sorted(save):
        acc += minutes
        total += acc
    
    print(total)
