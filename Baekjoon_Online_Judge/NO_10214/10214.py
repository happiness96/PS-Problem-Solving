# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 21                             | #
# | 10214 Baseball                      | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        tot_y, tot_k = 0, 0

        for _ in range(9):
            y, k = map(int, r_input().split())

            tot_y += y
            tot_k += k
        
        print("Yonsei" if tot_y > tot_k else "Korea" if tot_y < tot_k else "Draw")
