# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 05                             | #
# | 9417 최대 GCD                       | #
# -------------------------------------- #


def get_gcd(num1, num2):
    mod = num2 % num1
    
    if not mod:
        return num1
    
    else:
        return get_gcd(mod, num1)


if __name__ == "__main__":
    N = int(r_input())

    for _ in range(N):
        numbers = sorted(map(int, r_input().split()))
        length = len(numbers)
        res = 0

        for ind1, number1 in enumerate(numbers):
            for ind2 in range(ind1 + 1, length):
                res = max(res, get_gcd(number1, numbers[ind2]))
        
        print(res)
