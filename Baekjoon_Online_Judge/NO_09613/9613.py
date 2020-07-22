# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 22                   | #
# | 9613 GCD 합              | #
# ---------------------------- #


def get_gcd(num1, num2):
    mod = num2 % num1

    if mod == 0:
        return num1
    
    else:
        return get_gcd(mod, num1)


if __name__ == "__main__":
    t = int(r_input())

    for _ in range(t):
        num_list = list(map(int, r_input().split()))
        n = num_list.pop(0)
        
        num_list.sort()

        result = 0

        for ind1 in range(n):
            for ind2 in range(ind1 + 1, n):
                result += get_gcd(num_list[ind1], num_list[ind2])
        
        print(result)
