# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 17                             | #
# | 1451 직사각형으로 나누기             | #
# -------------------------------------- #


def run():
    N, M = map(int, r_input().split())

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for row in range(1, N + 1):
        line = [0] + list(r_input().rstrip())

        for col in range(1, M + 1):
            dp[row][col] = dp[row][col - 1] + dp[row - 1][col] - dp[row - 1][col - 1] + int(line[col])

    res = 0

    if N == 1:
        for i in range(1, M - 1):
            sq1 = dp[1][i]

            for j in range(i + 1, M):
                sq2 = dp[1][j] - sq1
                sq3 = dp[1][M] - sq1 - sq2

                res = max(res, sq1 * sq2 * sq3)
    
    elif M == 1:
        for i in range(1, N - 1):
            sq1 = dp[i][1]

            for j in range(i + 1, N):
                sq2 = dp[j][1] - sq1
                sq3 = dp[N][1] - sq1 - sq2
                res = max(res, sq1 * sq2 * sq3)

    else:
        for row in range(1, N + 1):
            for col in range(1, M + 1):
                sq1 = dp[row][col]
                sq2 = dp[row][M] - sq1
                sq3 = dp[N][col] - sq1
                sq4 = dp[N][M] - sq2 - sq3 - sq1

                res = max(res, (sq1 + sq2) * sq3 * sq4, (sq1 + sq3) * sq2 * sq4, (sq2 + sq4) * sq3 * sq1, sq1 * sq2 * (sq3 + sq4))
            
        for i in range(1, N - 1):
            for j in range(1, N):
                sq1 = dp[i][M]
                sq2 = dp[j][M] - sq1
                sq3 = dp[N][M] - sq1 - sq2

                res = max(res, sq1 * sq2 * sq3)
        
        for i in range(1, M - 1):
            for j in range(1, M):
                sq1 = dp[N][i]
                sq2 = dp[N][j] - sq1
                sq3 = dp[N][M] - sq1 - sq2

                res = max(res, sq1 * sq2 * sq3)
    
    print(res)


if __name__ == "__main__":
    run()
