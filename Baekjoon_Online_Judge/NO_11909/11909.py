# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 26                             | #
# | 11909 배열 탈출                     | #
# -------------------------------------- #


def run():
    n = int(r_input())
    line = list(map(int, r_input().split()))
    cost = [0] * n

    for ind in range(1, n):
        if line[ind] >= line[ind - 1]:
            cost[ind] = cost[ind - 1] + line[ind] - line[ind - 1] + 1
        
        else:
            cost[ind] = cost[ind - 1]

    for _ in range(n - 1):
        next_line = list(map(int, r_input().split()))

        if next_line[0] >= line[0]:
            cost[0] += next_line[0] - line[0] + 1
        
        for ind in range(1, n):
            cost[ind] = min(cost[ind] + max(0, next_line[ind] - line[ind] + 1), cost[ind - 1] + max(0, next_line[ind] - next_line[ind - 1] + 1))

        line = next_line

    print(cost[-1])


if __name__ == "__main__":
    run()
