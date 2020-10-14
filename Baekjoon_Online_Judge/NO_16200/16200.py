# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 16200 해커톤                        | #
# -------------------------------------- #


def run():
    N = int(r_input())

    X = sorted(map(int, r_input().split()))
    team_cnt = 0

    ind = 0

    while N > 0:
        min_cnt = X[ind]
        ind += min_cnt
        N -= min_cnt
        team_cnt += 1
    
    print(team_cnt)


if __name__ == "__main__":
    run()
