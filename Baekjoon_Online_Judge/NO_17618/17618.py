# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 21                             | #
# | 17618 신기한 수                      | #
# -------------------------------------- #


def run():
    N = int(r_input())
    
    save = [0] * (N + 1)
    res = 0

    for num in range(1, N + 1):
        tmp = save[num // 10] + num % 10
        save[num] = tmp

        if not num % tmp:
            res += 1
    
    print(res)


if __name__ == "__main__":
    run()
