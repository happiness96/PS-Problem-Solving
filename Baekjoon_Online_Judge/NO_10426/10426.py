# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 22                             | #
# | 10426 기념일 2                      | #
# -------------------------------------- #


if __name__ == "__main__":
    special_day, N = map(str, r_input().rstrip().split())

    N = int(N) - 1

    Y, M, D = map(int, special_day.split('-'))
    chk = Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0

    for _ in range(N):
        D += 1

        if M in [1, 3, 5, 7, 8, 10, 12] and D == 32 or M in [4, 6, 9, 11] and D == 31:
            D = 1
            M += 1

            if M == 13:
                M = 1
                Y += 1
                chk = Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0
        
        elif chk and M == 2 and D == 30 or not chk and M == 2 and D == 29:
            D = 1
            M += 1
    
    print('%04d-%02d-%02d' % (Y, M, D))
