# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 1138 한 줄로 서기                   | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())
    taller = list(map(int, r_input().split()))
    save = [0] * N

    for no, cnt in enumerate(taller):
        for ind in range(N):
            if save[ind]:
                continue
            
            if not cnt:
                save[ind] = no + 1
                break
            
            else:
                cnt -= 1
    
    print(*save)
