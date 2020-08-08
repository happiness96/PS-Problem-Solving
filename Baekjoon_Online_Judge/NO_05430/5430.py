# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 08                             | #
# | 5430 AC                            | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        p = r_input().rstrip()
        n = int(r_input())
        x = r_input().rstrip()[1: -1]

        x_list = []
        
        if x:
            x_list = deque(list(x.split(',')))

        err_flag = 0
        rev_flag = 0

        for command in p:
            if command == 'R':
                rev_flag = abs(rev_flag - 1)
            
            else:
                if not x_list:
                    err_flag = 1
                    break
                
                else:
                    if rev_flag: x_list.pop()
                    else: x_list.popleft()
        
        if err_flag:
            print('error')
        
        else:
            if rev_flag:
                x_list = list(x_list)[::-1]

            print('[' + ','.join(x_list) + ']')


if __name__ == "__main__":
    run()
