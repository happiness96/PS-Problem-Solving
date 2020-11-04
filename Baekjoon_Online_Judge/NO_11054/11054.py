# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 04                             | #
# | 11054 가장 긴 바이토닉 부분 수열     | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    A = list(map(int, r_input().split()))

    increasing = [0] * 1001
    increasing_dp = [0] * N
    decreasing = [0] * 1001
    decreasing_dp = [0] * N

    for ind, val in enumerate(A):
        tmp = max(increasing[: val]) + 1
        increasing[val] = tmp
        increasing_dp[ind] = tmp

    for ind in range(N - 1, -1, -1):
        val = A[ind]
        tmp = max(decreasing[: val]) + 1
        decreasing[val] = tmp
        decreasing_dp[ind] = tmp
    
    maxi = 0

    for ind in range(N):
        maxi = max(maxi, increasing_dp[ind] + decreasing_dp[ind])

    print(maxi - 1)
