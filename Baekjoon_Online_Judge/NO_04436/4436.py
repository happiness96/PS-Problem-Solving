# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 05                             | #
# | 4436 엘프의 검                      | #
# -------------------------------------- #


if __name__ == "__main__":
    for n in sys.stdin:
        n = int(n)
        chk = [0] * 10

        k = 1

        while True:
            for val in str(n * k):
                chk[int(val)] = 1

            if chk.count(0):
                k += 1
            
            else:
                break
        
        print(k)
