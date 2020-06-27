# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 27                   | #
# | 3035 스캐너               | #
# ---------------------------- #


if __name__ == "__main__":
    R, C, ZR, ZC = map(int, r_input().split())
    
    for _ in range(R):
        line = r_input().rstrip()

        for _ in range(ZR):
            for ch in line:
                print(ch * ZC, end='')
            
            print()
