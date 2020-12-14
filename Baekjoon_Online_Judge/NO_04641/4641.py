# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 14                             | #
# | 4641 Doubles                       | #
# -------------------------------------- #


if __name__ == "__main__":
    while True:
        numbers = list(map(int, r_input().split()))

        if numbers == [-1]:
            break
    
        cnt = 0

        for number in numbers:
            cnt += int(number * 2 in numbers)
        
        print(cnt - 1)