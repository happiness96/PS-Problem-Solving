# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 22                             | #
# | 10708 크리스마스 파티               | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    M = int(r_input())
    A = list(map(int, r_input().split()))

    scores = [0] * N

    for game_ind, target in enumerate(A):
        B = list(map(int, r_input().split()))

        get_score = 0

        for player_ind, guess in enumerate(B):
            if target == guess:
                scores[player_ind] += 1
                get_score += 1

        X = N - get_score

        scores[target - 1] += X
    
    print(*scores, sep='\n')
