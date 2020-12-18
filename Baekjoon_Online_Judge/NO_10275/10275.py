# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 16                             | #
# | 10275 골드 러시                    | #
# -------------------------------------- #

def run():
    t = int(r_input())

    for _ in range(t):
        n, a, b = map(int, r_input().split())

        cnt = 0
        bin_a = bin(a)[2:]

        for ch in bin_a[::-1]:
            if ch == '0':
                cnt += 1
            
            else:
                break
        
        print(n - cnt)


if __name__ == "__main__":
    run()
