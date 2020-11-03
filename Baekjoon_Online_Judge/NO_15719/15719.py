# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 03                             | #
# | 15719 중복된 숫자                   | #
# -------------------------------------- #


def run():
    N = int(r_input())

    N *= (N - 1)
    N //= 2

    tot = 0
    save = ''

    for val in sys.stdin.read():
        if val == ' ':
            tmp = int(save)
            tot += tmp

            save = ''
        
        else:
            save += val
    
    tot += int(save)
    print(tot - N)


if __name__ == "__main__":
    run()
