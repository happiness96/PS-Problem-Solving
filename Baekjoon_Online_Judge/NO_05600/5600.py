# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 06                 | #
# | Day 29                   | #
# | 5600 품질 검사            | #
# ---------------------------- #


if __name__ == "__main__":
    a, b, c = map(int, r_input().split())

    N = int(r_input())
    res = [2] * (a + b + c + 1)
    zero = []

    for _ in range(N):
        i, j, k, r = map(int, r_input().split())
        
        if r:
            res[i] = 1
            res[j] = 1
            res[k] = 1
        
        else:
            zero.append((i, j, k))
    
    for i, j, k in zero:
        if res[i] == res[j] == 1:
            res[k] = 0
        
        elif res[j] == res[k] == 1:
            res[i] = 0
        
        elif res[i] == res[k] == 1:
            res[j] = 0

    print(*res[1:], sep='\n')
