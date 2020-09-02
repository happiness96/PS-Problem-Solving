# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 소수 찾기                           | #
# -------------------------------------- #


if __name__ == "__main__":
    prime = [1] * 1001
    prime[1] = 0

    for i in range(4, 1001, 2):
        prime[i] = 0
    
    for i in range(3, 1001, 2):
        for rem in range(i * 2, 1001, i):
            prime[rem] = 0

    N = int(r_input())
    res = 0

    for num in map(int, r_input().split()):
        res += prime[num]

    print(res)
