# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 04                             | #
# | 받아올림                            | #
# -------------------------------------- #


if __name__ == "__main__":
    while True:
        num1, num2 = map(int, r_input().split())

        if num1 == num2 == 0:
            break
        
        if num1 < num2: num1, num2 = num2, num1

        num1 = str(num1)[::-1]
        num2 = str(num2)[::-1]
        len1 = len(num1)
        len2 = len(num2)

        res = 0
        up = 0

        for ind in range(len1):
            if ind < len2:
                tmp = int(num1[ind]) + int(num2[ind]) + up

                if tmp >= 10:
                    up = 1
                    res += 1
            
            else:
                tmp = int(num1[ind]) + up

                if tmp == 10:
                    up = 1
                    res += 1
        
        print(res)
