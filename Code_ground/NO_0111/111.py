# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 25                   | #
# | 파티셰리                   | #
# ---------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for testcase in range(1, T + 1):
        N = int(r_input())

        d, c, m = 11, 9, 7

        res = 'NO'

        for ind1 in range(100 // d):
            for ind2 in range(100 // c):
                for ind3 in range(100 // m):
                    if ind1 * d + ind2 * c + ind3 * m == N:
                        res = 'YES'
                        break
                
                if res == 'YES':
                    break
            
            if res == 'YES':
                break
        
        print('Case #' + str(testcase))
        print(res)
