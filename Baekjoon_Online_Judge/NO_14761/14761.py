# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 03                             | #
# | 14761 FizBuzz                      | #
# -------------------------------------- #


if __name__ == "__main__":
    X, Y, N = map(int, r_input().split())

    for number in range(1, N + 1):
        fizz = number % X
        buzz = number % Y

        if fizz == buzz == 0:
            print('FizzBuzz')
        
        elif fizz == 0:
            print('Fizz')
        
        elif buzz == 0:
            print('Buzz')
        
        else:
            print(number)
