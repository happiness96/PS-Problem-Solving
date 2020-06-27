# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 10162 전자레인지           | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    btn1 = T // 300
    T %= 300

    btn2 = T // 60
    T %= 60

    btn3 = T // 10
    T %= 10

    if T:
        print(-1)
    
    else:
        print(btn1, btn2, btn3)
