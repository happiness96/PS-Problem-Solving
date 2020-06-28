# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 28                   | #
# | 1173 운동                 | #
# ---------------------------- #


def run():
    N, m, M, T, R = map(int, r_input().split())

    pulse = m

    if m + T > M:
        print(-1)
    
    else:
        minutes = 0

        while N:
            if pulse + T > M:
                pulse = max(pulse - R, m)
            
            else:
                pulse += T
                N -= 1
            
            minutes += 1
        
        print(minutes)


if __name__ == "__main__":
    run()
