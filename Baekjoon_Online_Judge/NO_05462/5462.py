# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 5462 POI                          | #
# -------------------------------------- #


def run():
    N, T, P = map(int, r_input().split())

    scores = [0] * N
    solved_cnt = [0] * N
    status = [list(map(int, r_input().split())) for _ in range(N)]

    for problem_no in range(T):
        sc = 0

        for st_no in range(N):
            sc += abs(status[st_no][problem_no] - 1)
        
        for st_no in range(N):
            if status[st_no][problem_no]:
                scores[st_no] += sc
                solved_cnt[st_no] += 1
    
    P -=1
    P = -P
    
    sort_rank = []

    for st_no in range(N):
        sort_rank.append((scores[st_no], solved_cnt[st_no], -st_no))
    
    sort_rank.sort(reverse=True)

    for rank, st_status in enumerate(sort_rank):
        st_score, _, st_no = st_status

        if st_no == P:
            print(st_score, rank + 1)
            break


if __name__ == "__main__":
    run()
