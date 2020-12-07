# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 07                             | #
# | 12840 창용이의 시계                 | #
# -------------------------------------- #


def run():
    h, m, s = map(int, r_input().split())

    tc = int(r_input())

    for _ in range(tc):
        query = r_input().rstrip()

        if query == '3':
            p_m = s // 60
            s %= 60
            m += p_m
            p_h = m // 60
            m %= 60
            h += p_h
            h %= 24
            print(h, m, s)
        
        else:
            t, c = map(int, query.split())

            if t == 1:
                s += c
            
            else:
                s -= c


if __name__ == "__main__":
    run()
