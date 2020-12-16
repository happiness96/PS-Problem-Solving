# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 15                             | #
# | 6504 킬로미터를 마일로              | #
# -------------------------------------- #


def run():
    t = int(r_input())

    fibo = [1, 2]

    while fibo[-1] < 25000:
        fibo.append(fibo[-1] + fibo[-2])
    
    for _ in range(t):
        x = int(r_input())

        save = []

        for ind, val in enumerate(fibo[::-1]):
            if val <= x:
                x -= val
                save.append('1')
            
            else:
                save.append('0')
        
        res = str(int(''.join(save)[:-1]))[::-1]
        result = 0

        for ind, val in enumerate(res):
            if val == '1':
                result += fibo[ind]
        
        print(result)


if __name__ == "__main__":
    run()
