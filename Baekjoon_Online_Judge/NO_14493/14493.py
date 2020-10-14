# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 14                             | #
# | 14493 과일노리                      | #
# -------------------------------------- #


def run():
    N = int(r_input())

    time = 0

    for _ in range(N):
        a, b = map(int, r_input().split())
        tot_time = a + b
        tmp_time = time % tot_time

        if tmp_time < b:
            time += b - tmp_time

        time += 1
    
    print(time)


if __name__ == "__main__":
    run()
