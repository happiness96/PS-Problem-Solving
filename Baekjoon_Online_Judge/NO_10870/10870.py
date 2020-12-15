# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 10870 피보나치 수 5                 | #
# -------------------------------------- #


if __name__ == "__main__":
    def fibo(number):
        if number == 0:
            return 0
        
        elif number == 1:
            return 1
        
        else:
            return fibo(number - 1) + fibo(number - 2)
    
    N = int(r_input())
    print(fibo(N))
