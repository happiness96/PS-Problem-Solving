# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 01                             | #
# | 11916 불질                         | #
# -------------------------------------- #


def on_base():
    global loss
    
    if base[0]:
        if base[1]:
            if base[2]:
                loss += 1
            base[2] = 1
        base[1] = 1
    base[0] = 1


if __name__ == "__main__":
    N = int(r_input())

    balls = list(map(int, r_input().split()))
    ball_cnt = 0
    base = [0, 0, 0]
    loss = 0

    for ball in balls:
        if ball == 1:
            ball_cnt += 1

            if ball_cnt == 4:
                ball_cnt = 0

                on_base()
        
        elif ball == 2:
            ball_cnt = 0

            on_base()
        
        else:
            ball_cnt += 1

            if base[2]:
                loss += 1
            
            base = [0] + base[: 2]

            if ball_cnt == 4:
                base[0] = 1
                ball_cnt = 0
    
    print(loss)
