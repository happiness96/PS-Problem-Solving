# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 05                 | #
# | Day 24                   | #
# | 1652 누울 자리를 찾아라     | #
# ---------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    room = [list(r_input().rstrip()) for _ in range(N)]

    garo, sero = 0, 0

    for row in range(N):
        count = 0

        for col in range(N):
            if room[row][col] == '.':
                count += 1
            
            else:
                if count >= 2:
                    garo += 1
                
                count = 0

        if count >= 2:
            garo += 1
    
    for col in range(N):
        count = 0

        for row in range(N):
            if room[row][col] == '.':
                count += 1
            
            else:
                if count >= 2:
                    sero += 1
                
                count = 0
        
        if count >= 2:
            sero += 1
    
    print(garo, sero)