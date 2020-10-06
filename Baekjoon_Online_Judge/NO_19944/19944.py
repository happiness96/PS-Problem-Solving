# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19944 뉴비의 기준은 뭘까?            | #
# -------------------------------------- #


if __name__ == "__main__":
    N, M = map(int, r_input().split())

    print('NEWBIE!' if M < 3 else 'OLDBIE!' if M <= N else 'TLE!')
