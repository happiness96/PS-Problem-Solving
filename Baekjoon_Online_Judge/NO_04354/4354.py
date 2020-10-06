# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 05                             | #
# | 4354 문자열 제곱                    | #
# -------------------------------------- #


def run():
    while True:
        s = r_input().rstrip()

        if s == '.':
            break

        length = len(s)
        
        flag = 0

        for i in range(1, length // 2 + 1):
            if length % i == 0:
                div = length // i

                if s[:i] * div == s:
                    flag = div
                    break
        
        print(flag if flag else 1)


if __name__ == "__main__":
    run()
