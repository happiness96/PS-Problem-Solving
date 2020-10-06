# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 06                             | #
# | 19949 영재의 시험                   | #
# -------------------------------------- #


def get_scores(select, selected):
    global res

    selected.append(select)
    length = len(selected)

    if length == 10:
        score = 0

        for ind, ans in enumerate(selected):
            if ans == answer[ind]:
                score += 1
        
        if score >= 5:
            res += 1
    
    else:
        for num in range(1, 6):
            if length >= 2 and selected[-1] == selected[-2] == num:
                continue

            get_scores(num, selected)
    
    selected.pop()


if __name__ == "__main__":
    answer = list(map(int, r_input().split()))
    res = 0

    for num in range(1, 6):
        get_scores(num, [])

    print(res)
