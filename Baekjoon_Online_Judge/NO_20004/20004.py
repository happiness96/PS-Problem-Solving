# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 20004 베스킨라빈스 31                | #
# -------------------------------------- #


if __name__ == "__main__":
    A = int(r_input())

    for num in range(1, A + 1):
        save = [30]

        while True:
            tmp = save[-1] - num - 1

            if tmp < 1:
                break

            save.append(tmp)
        
        if save[-1] <= num:
            continue
        
        else:
            print(num)
