# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 23                   | #
# | 프로그래밍 경진대회          | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for testcase in range(1, T + 1):
        N = int(r_input())

        score = [int(r_input()) for _ in range(N)]
        score.sort()
        
        res = 0
        mx_cnt = score.count(score[-1])

        for ind in range(N - 1):
            if score[ind] + N >= score[-1] + mx_cnt:
                res += 1
                

        print('Case #' + str(testcase))
        print(res + 1)