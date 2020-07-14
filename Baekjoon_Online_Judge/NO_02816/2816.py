# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 14                   | #
# | 2816 디지털 티비           | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    KBS1 = 0
    KBS2 = 0

    for ind in range(N):
        channel = r_input().rstrip()

        if channel == 'KBS1':
            KBS1 = ind
        
        elif channel == 'KBS2':
            KBS2 = ind
    
    flag = int(KBS1 > KBS2)
    print('1' * KBS1 + '4' * KBS1, end='')

    KBS2 += flag
    print('1' * KBS2 + '4' * (KBS2 - 1))
