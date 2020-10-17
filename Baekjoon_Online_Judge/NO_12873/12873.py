# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 17                             | #
# | 12873 기념품                        | #
# -------------------------------------- #


def run():
    N = int(r_input())

    members = list(range(N))
    pop_ind = 0
    entire_member = N

    for step in range(1, N):
        pop_ind += step ** 3 - 1
        pop_ind %= entire_member

        members.pop(pop_ind)
        entire_member -= 1
    
    print(members[0] + 1)


if __name__ == "__main__":
    run()
