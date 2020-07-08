# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 1145 적어도 대부분의 배수   | #
# ---------------------------- #


def get_gcd(num1, num2):
    mod = num2 % num1

    if not mod:
        return num1
    
    else:
        return get_gcd(mod, num1)


if __name__ == "__main__":
    numbers = sorted(map(int, r_input().split()))
    result = sys.maxsize

    for case in combinations(numbers, 3):
        case = list(case)
        gcd1 = get_gcd(case[0], case[1])
        tmp = case[0] // gcd1 * case[1]

        gcd2 = get_gcd(tmp, case[2]) if tmp <= case[2] else get_gcd(case[2], tmp)

        result = min(result, tmp // gcd2 * case[2])
    
    print(result)
