# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 14                             | #
# | 6068 시간 관리하기                  | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    
    save = []

    for _ in range(N):
        T, S = map(int, r_input().split())
        save.append((S, T))
    
    save.sort()
    cur_time = sys.maxsize

    while save:
        S, T = save.pop()
        cur_time = min(cur_time, S) - T
    
    print(max(-1, cur_time))
