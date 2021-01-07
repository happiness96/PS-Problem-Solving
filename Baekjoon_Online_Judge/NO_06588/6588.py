# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 07                             | #
# | 6588 골드바흐의 추측                | #
# -------------------------------------- #


def run():
    primes = [1] * 1000001

    primes[0] = 0
    primes[1] = 0

    for num in range(4, 1000001, 2):
        primes[num] = 0

    for num in range(3, int(1000001 ** 0.5) + 1, 2):
        if primes[num]:
            for rem in range(num * 2, 1000001, num):
                primes[rem] = 0
    
    while True:
        number = int(r_input())
        
        if not number:
            break
        
        for ind, val in enumerate(primes):
            if val and primes[number - ind]:
                print(str(number) + ' = ' + str(ind) + ' + ' + str(number - ind))
                break


if __name__ == "__main__":
    run()
