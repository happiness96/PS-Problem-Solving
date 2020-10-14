# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 14655 욱제는 도박쟁이야!!            | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    round1 = list(map(int, r_input().split()))
    round2 = list(map(int, r_input().split()))

    maxi = 0
    mini = 0

    for ind in range(N):
        maxi += abs(round1[ind])
        mini -= abs(round2[ind])
    
    print(maxi - mini)
