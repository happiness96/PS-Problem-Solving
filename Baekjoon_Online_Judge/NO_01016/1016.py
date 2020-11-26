# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 26                             | #
# | 1016 제곱 ㄴㄴ 수                   | #
# -------------------------------------- #


def run():
    mini, maxi = map(int, r_input().split())

    dp = [1] * (maxi - mini + 1)

    number = 2

    while True:
        div = number ** 2

        if div > maxi:
            break

        start = (mini // div + int(mini % div != 0)) * div

        for ind in range(start, maxi + 1, div):
            dp[ind - mini] = 0

        number += 1

    print(sum(dp))


if __name__ == "__main__":
    run()
