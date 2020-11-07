# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 07                             | #
# | 4383 점프는 즐거워                   | #
# -------------------------------------- #


def run():
    for line in sys.stdin:
        n, *jolly = map(int, line.split())

        chk = [0] * n

        for i in range(n - 1):
            diff = abs(jolly[i] - jolly[i + 1])

            if diff < n:
                chk[diff] = 1
        
        if chk != [0] + [1] * (n - 1):
            print('Not jolly')
        
        else:
            print('Jolly')

if __name__ == "__main__":
    run()
