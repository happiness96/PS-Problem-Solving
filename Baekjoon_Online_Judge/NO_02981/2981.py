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

    gaps = []

    for i in range(1, N):
        gaps.append(numbers[i] - numbers[i - 1])
    
    gaps.sort()

    gap = gaps[0]

    for i in range(1, len(gaps)):
        gap = get_gcd(gap, gaps[i])
    
    res = set()

    for i in range(2, int(gap ** 0.5) + 1):
        if gap % i == 0:
            res.add(i)
            res.add(gap // i)

    res.add(gap)
    print(*sorted(res))
