# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 9329 패스트 푸드 상금               | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        n, m = map(int, r_input().split())
        save = []

        for _ in range(n):
            _, *for_win, score = list(map(int, r_input().split()))
            save.append([for_win, score])
        
        stickers = [0] + list(map(int, r_input().split()))
        total_score = 0

        for for_win, score in save:
            max_cnt = sys.maxsize

            for ind in for_win:
                max_cnt = min(max_cnt, stickers[ind])
            
            total_score += score * max_cnt
        
        print(total_score)
