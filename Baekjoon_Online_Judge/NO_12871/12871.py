# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------   --------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 23                   | #
# | 12871 무한 문자열          | #
# ---------------------------- #


def run():
    s = r_input().rstrip()
    t = r_input().rstrip()
    
    len_s = len(s)
    len_t = len(t)

    print(int(s * len_t == t * len_s))
    

if __name__ == "__main__":
    run()
