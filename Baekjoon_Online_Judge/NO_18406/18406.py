# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 27                   | #
# | 18406 럭키 스트레이트       | #
# ---------------------------- #


if __name__ == "__main__":
    N = r_input().rstrip()

    tot1 = 0
    tot2 = 0

    for val in N[:len(N) // 2]:
        tot1 += int(val)
    
    for val in N[len(N) // 2:]:
        tot2 += int(val)
    
    print('LUCKY' if tot1 == tot2 else 'READY')
