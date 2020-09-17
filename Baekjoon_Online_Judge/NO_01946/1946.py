# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 17                             | #
# | 1946 신입사원                       | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())

        score = [0] * (N + 1)

        for _ in range(N):
            score1, score2 = map(int, r_input().split())

            score[score1] = score2

        res = 0
        tmp = N + 1

        for ind in range(1, N + 1):
            if score[ind] < tmp:
                res += 1
                tmp =score[ind]
        
        print(res)


if __name__ == "__main__":
    run()
