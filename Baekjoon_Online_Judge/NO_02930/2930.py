# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 24                             | #
# | 2930 가위 바위 보                   | #
# -------------------------------------- #


if __name__ == "__main__":
    R = int(r_input())
    sg = r_input().rstrip()

    N = int(r_input())
    score = 0

    save = [[0, 0, 0] for _ in range(R)]

    for _ in range(N):
        fr = r_input().rstrip()

        for ind, val in enumerate(fr):
            save[ind]['RSP'.index(val)] += 1
        
        for ind, val in enumerate(sg):
            if val == fr[ind]:
                score += 1
            
            elif (val, fr[ind]) in [('S', 'P'), ('P', 'R'), ('R', 'S')]:
                score += 2

    max_score = 0

    for val in save:
        max_score += max(val[0] + val[1] * 2, val[1] + val[2] * 2, val[2] + val[0] * 2)
    
    print(score)
    print(max_score)
