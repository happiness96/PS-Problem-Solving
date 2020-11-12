# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 12                             | #
# | 2246 콘도 선정                      | #
# -------------------------------------- #


def run():
    N = int(r_input())

    save1 = []
    save2 = []
    res = [0] * N

    for ind in range(N):
        D, C = map(int, r_input().split())
        save1.append((D, C, ind))
        save2.append((C, D, ind))
    
    save1.sort()
    save2.sort()
    
    mini = sys.maxsize
    tmp_d = 0
    tmp_c = sys.maxsize

    for d, c, ind in save1:
        if d > tmp_d:
            mini = min(mini, tmp_c)

            tmp_d = d
            tmp_c = c

        if c < mini:
            res[ind] = 1
    
    mini = sys.maxsize
    tmp_c = 0
    tmp_d = sys.maxsize
    cnt = 0
    
    for c, d, ind in save2:
        if c > tmp_c:
            mini = min(mini, tmp_d)

            tmp_c = c
            tmp_d = d

        if d < mini:
            if res[ind]:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    run()
