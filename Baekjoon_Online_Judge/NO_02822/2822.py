# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 08                 | #
# | Day 02                   | #
# | 2822 점수 계산             | #
# ---------------------------- #


if __name__ == "__main__":
    scores = []
    
    for ind in range(1, 9):
        score = int(r_input())

        scores.append([score, ind])
    
    scores.sort()
    total = 0
    res = []

    for ind in range(3, 8):
        total += scores[ind][0]
        res.append(scores[ind][1])
    
    print(total)
    print(*sorted(res))
