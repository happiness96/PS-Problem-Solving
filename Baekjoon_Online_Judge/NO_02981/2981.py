# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 16                             | #
# | 2981 검문                          | #
# -------------------------------------- #


def get_gcd(num1, num2):
    rem = num2 % num1

    if rem == 0:
        return num1
    
    else:
        return get_gcd(rem, num1)


if __name__ == "__main__":
    N = int(r_input())

    numbers = [int(r_input()) for _ in range(N)]
    numbers.sort()

    gaps = set()

    for i in range(1, N):
        gaps.add(numbers[i] - numbers[i - 1])
    
    gaps = list(gaps)
    
    while len(gaps) != 1:
        gaps.sort()
        new_gaps = []

        for i in range(1, len(gaps)):
            new_gaps.append(get_gcd(gaps[i - 1], gaps[i]))
        
        gaps = sorted(set(new_gaps))
    
    res = gaps[0]

    for num in range(2, res // 2 + 1):
        if res % num == 0:
            print(num, end=' ')
    
    print(res)
