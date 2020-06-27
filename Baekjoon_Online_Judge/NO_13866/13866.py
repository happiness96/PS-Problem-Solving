# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 13866 팀 나누기           | #
# ---------------------------- #


if __name__ == "__main__":
    A, B, C, D = map(int, r_input().split())
    
    print(abs(D + A - C - B))
