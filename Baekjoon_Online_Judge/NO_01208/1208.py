# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 1208 부분수열의 합 2                 | #
# -------------------------------------- #


def run():
    N, S = map(int, r_input().split())

    negative_A = []
    positive_A = []

    for val in map(int, r_input().split()):
        if val < 0:
            negative_A.append(val)
        
        else:
            positive_A.append(val)
        
    make_positive = 4000000

    dp = [0] * 8000001
    S += make_positive
    
    for val in negative_A:
        for ind, dp_val in enumerate(dp):
            if dp_val:
                tmp_ind = ind + val

                if tmp_ind >= 0:
                    dp[tmp_ind] += dp_val

        dp[val + make_positive] += 1
    
    for val in positive_A:
        for ind in range(8000000, -1, -1):
            if dp[ind]:
                tmp_ind = ind + val

                if tmp_ind <= 8000000:
                    dp[tmp_ind] += dp[ind]
        
        dp[val + make_positive] += 1
    
    print(dp[S])


if __name__ == "__main__":
    run()
