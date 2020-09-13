# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 13                             | #
# | 15624 피보나치 수 7                 | #
# -------------------------------------- #


def run():
    n = int(r_input())
    
    a, b = 0, 1

    if n == 0:
        print(a)
    
    else:
        for _ in range(n - 1):
            a, b = b, (a + b) % 1000000007
        
        print(b)


if __name__ == "__main__":
    run()
