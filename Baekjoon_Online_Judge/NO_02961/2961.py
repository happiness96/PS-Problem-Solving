# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 15                             | #
# | 2961 도영이가 만든 맛있는 음식      | #
# -------------------------------------- #


def select(selected, tot_S, tot_B):
    global res

    tot_S *= foods[selected][0]
    tot_B += foods[selected][1]

    diff = abs(tot_S - tot_B)

    res = min(res, diff)

    for ind in range(selected + 1, N):
        select(ind, tot_S, tot_B)


if __name__ == "__main__":
    N = int(r_input())

    foods = []

    for _ in range(N):
        S, B = map(int, r_input().split())
        foods.append((S, B))
    
    res = sys.maxsize

    for ind in range(N):
        select(ind, 1, 0)
    
    print(res)
