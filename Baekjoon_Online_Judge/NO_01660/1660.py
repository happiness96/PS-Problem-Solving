# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 15                   | #
# | 1660 캡틴 이다솜           | #
# ---------------------------- #


def run():
    N = int(r_input())

    need = [0]

    for i in range(1, 122):
        need.append(need[-1] + i)
    
    for i in range(1, 122):
        need[i] += need[i - 1]
    
    rem = [sys.maxsize] * (N + 1)
    rem[-1] = 0

    for ind in range(N, 0, -1):
        if rem[ind] == sys.maxsize:
            continue
        for val in need:
            next_ind = ind - val

            if next_ind >= 0:
               rem[next_ind] = min(rem[next_ind], rem[ind] + 1)
            
            else:
                break
    
    print(rem[0])


if __name__ == "__main__":
    run()
