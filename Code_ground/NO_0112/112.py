# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 24                   | #
# | 플레이버튼                 | #
# ---------------------------- #


def run():
    T = int(r_input())

    for testcase in range(1, T + 1):
        subscriber = int(r_input())

        print('Case #' + str(testcase))

        if subscriber < 100000:
            print('NONE')
        
        elif subscriber < 1000000:
            print('SILVER')
        
        elif subscriber < 10000000:
            print('GOLD')
        
        else:
            print('DIAMOND')


if __name__ == "__main__":
    run()
