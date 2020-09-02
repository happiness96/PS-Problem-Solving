# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 02                             | #
# | 한수                                | #
# -------------------------------------- #


if __name__ == "__main__":
    res = [0] * 1001

    for val in range(1, 1001):
        flag = 1

        str_val = str(val)
        length = len(str_val)

        if length > 2:
            gap = int(str_val[0]) - int(str_val[1])

            for ind in range(2, length):
                s_gap = int(str_val[ind - 1]) - int(str_val[ind])

                if s_gap  != gap:
                    flag = 0
                    break
        
        res[val] = flag
    
    N = int(r_input())
    print(sum(res[: N + 1]))
