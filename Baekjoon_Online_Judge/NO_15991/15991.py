# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 12                             | #
# | 15991 1, 2, 3 더하기 6             | #
# -------------------------------------- #


def run():
    # 홀수이면서 가운데가 1, 2, 3인 것의 개수, 짝수
    dp = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0]]

    for num in range(4, 100001):
        tmp = [0, 0, 0, 0]

        for p in range(1, 4):
            tmp[3] += dp[-p][p - 1]
            tmp[p - 1] = dp[-p][3]
        
        for p in range(4):
            tmp[p] %= 1000000009
        
        dp.append(tmp)

    T = int(r_input())

    for _ in range(T):
        n = int(r_input())
        print(sum(dp[n]) % 1000000009)


if __name__ == "__main__":
    run()
