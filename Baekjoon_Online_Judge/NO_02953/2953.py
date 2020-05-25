# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 2953 나는 요리사다         | #
# ---------------------------- #


if __name__ == "__main__":
    winner = 0
    winner_score = -1

    for ind in range(1, 6):
        total_score = sum(map(int, r_input().split()))

        if total_score > winner_score:
            winner_score = total_score
            winner = ind
    
    print(winner, winner_score)
