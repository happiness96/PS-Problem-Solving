# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 04                             | #
# | 4948 베트르당 공준                  | #
# -------------------------------------- #


if __name__ == "__main__":
    dp = [1] * (123456 * 2)
    dp[0] = 0
    dp[1] = 0

    for number in range(4, 123456 * 2, 2):
        dp[number] = 0

    for number in range(3, int((123456 * 2) ** 0.5), 2):
        if dp[number]:
            for rem in range(number * 2, 123456 * 2, number):
                dp[rem] = 0

    while True:
        n = int(r_input())

        if not n:
            break
        
        print(sum(dp[n + 1: 2 * n + 1]))
