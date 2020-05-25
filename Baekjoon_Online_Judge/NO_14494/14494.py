# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 14494 다이나믹이 뭐예요?    | #
# ---------------------------- #


def run():
    n, m = map(int, r_input().split())

    dp = [1] * m

    for _ in range(n - 1):
        save = 1

        for ind in range(1, m):
            n_save = dp[ind]
            dp[ind] += save + dp[ind - 1]
            dp[ind] %= 1000000007
            save = n_save
        
    print(dp[m-1])


if __name__ == "__main__":
    run()
