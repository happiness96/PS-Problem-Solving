# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 명령 프롬프트                       | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    form = list(r_input().rstrip())

    for _ in range(N - 1):
        file_name = r_input().rstrip()

        for ind, val in enumerate(file_name):
            if val != form[ind]:
                form[ind] = '?'

    print(''.join(form))
