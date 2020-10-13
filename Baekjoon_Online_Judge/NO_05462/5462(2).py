# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 5462 POI                           | #
# -------------------------------------- #


def run():
    N, T, P = map(int, r_input().split())

    solved_cnt = [0] * N
    status = [[0] * N for _ in range(T)]

    for st_no in range(N):
        line = list(map(int, r_input().split()))

        for pb_no, val in enumerate(line):
            status[pb_no][st_no] = val
            solved_cnt[st_no] += val

    scores = [0] * N

    for pb_no, solve_status in enumerate(status):
        score = status[pb_no].count(0)

        for st_no, is_solve in enumerate(solve_status):
            if is_solve:
                scores[st_no] += score
    
    rank = 1
    P -= 1
    P_score, P_solved = scores[P], solved_cnt[P]

    for st_no in range(N):
        if scores[st_no] > P_score or scores[st_no] == P_score and solved_cnt[st_no] > P_solved or scores[st_no] == P_score and solved_cnt[st_no] == P_solved and st_no < P:
            rank +=1

    print(P_score, rank)


if __name__ == "__main__":
    run()
