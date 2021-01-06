# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 06                             | #
# | 1241 머리 톡톡                      | #
# -------------------------------------- #


def get_divisor(num):
    divisors = set()

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)

    return divisors

def run():
    primes = [1] * 500001

    N = int(r_input())

    save = [0] * 1000001
    numbers = []

    for _ in range(N):
        number = int(r_input())
        numbers.append(number)
        save[number] += 1
    
    for number in numbers:
        result = 0
        
        for m in get_divisor(number):
            result += save[m]
        
        print(result - 1)


if __name__ == "__main__":
    run()
