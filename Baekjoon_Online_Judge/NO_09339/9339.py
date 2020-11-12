# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 12                             | #
# | 9339 마라토너                       | #
# -------------------------------------- #


def run():
    T = int(r_input())
    six_h = 360

    for _ in range(T):
        K = int(r_input())
        participants = set(map(int, r_input().split()))

        N = int(r_input())
        res = 0
        cnt = 0
        best = sys.maxsize

        for _ in range(N):
            participant, h, m = map(int, r_input().split())

            if participant in participants:
                time = h * 60 + m

                if time < 0:
                    continue

                if time < best:
                    best = time
                    res = participant
                
                if time <= six_h:
                    cnt += 1
            
        print(res, cnt)


if __name__ == "__main__":
    run()
