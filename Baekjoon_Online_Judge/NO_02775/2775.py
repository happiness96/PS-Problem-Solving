# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 30                             | #
# | 2775 부녀회장이 될테야              | #
# -------------------------------------- #


if __name__ == "__main__":
    T = int(r_input())

    for _ in range(T):
        k = int(r_input())
        n = int(r_input())

        pre_floor = list(range(n + 1))

        for _ in range(k):
            cur_floor = [0]

            for ind in range(1, n + 1):
                cur_floor.append(cur_floor[-1] + pre_floor[ind])
            
            pre_floor = cur_floor
            
        print(pre_floor[-1])
