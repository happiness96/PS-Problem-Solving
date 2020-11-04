# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 04                             | #
# | 20055 컨베이어 벨트 위의 로봇        | #
# -------------------------------------- #


def run():
    N, K = map(int, r_input().split())

    A = list(map(int, r_input().split()))
    robots = [0] * N
    step = 1

    while True:
        A = [A[-1]] + A[: -1]
        robots = [0] + robots[: -1]

        robots[N - 1] = 0

        for ind in range(N - 2, -1, -1):
            next_ind = ind + 1
            if robots[ind]:
                if not robots[next_ind] and A[next_ind]:
                    robots[ind] = 0
                    robots[next_ind] = 1
                    A[next_ind] -= 1
        
        if not robots[0] and A[0]:
            robots[0] = 1
            A[0] -= 1

        if A.count(0) >= K:
            print(step)
            break

        step += 1


if __name__ == "__main__":
    run()