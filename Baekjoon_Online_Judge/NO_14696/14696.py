# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 14                             | #
# | 14696 딱지놀이                     | #
# -------------------------------------- #


if __name__ == "__main__":
    N = int(r_input())

    for _ in range(N):
        a, *a_scab = list(map(int, r_input().split()))
        b, *b_scab = list(map(int, r_input().split()))

        a_count = {4: 0, 3: 0, 2: 0, 1: 0}
        b_count = {4: 0, 3: 0, 2: 0, 1: 0}

        for scab in a_scab:
            a_count[scab] += 1
        
        for scab in b_scab:
            b_count[scab] += 1
        
        flag = 0
        
        for num in range(4, 0, -1):
            if a_count[num] > b_count[num]:
                print('A')
                flag = 1
                break
            
            if a_count[num] < b_count[num]:
                print('B')
                flag = 1
                break
            
        if not flag:
            print('D')
