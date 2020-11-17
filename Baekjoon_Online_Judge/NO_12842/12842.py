# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 12                             | #
# | 12842 튀김 소보루                   | #
# -------------------------------------- #


def run():
    n, s = map(int, r_input().split())
    rem = n - s
    
    m = int(r_input())
    t = []
    save = [[] for _ in range(100000)]

    for i in range(m):
        val = int(r_input())
        t.append(val)
        save[0].append(i)
    
    for ind, val_list in enumerate(save):
        for val in sorted(val_list):
            rem -= 1

            if not rem:
                print(val + 1)
                sys.exit()
            
            save[ind + t[val]].append(val)


if __name__ == "__main__":
    run()
