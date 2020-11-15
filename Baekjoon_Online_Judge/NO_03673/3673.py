# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 11                           | #
# | Day 14                             | #
# | 3673 나눌 수 있는 부분 수열         | #
# -------------------------------------- #


def run():
    c = int(r_input())

    for _ in range(c):
        d, n = map(int, r_input().split())
        result = 0

        save = [0] * d
        save[0] = 1
        acc = 0

        for val in map(int, r_input().split()):
            val %= d

            acc += val
            acc %= d

            result += save[acc]
            save[acc] += 1
        
        print(result)


if __name__ == "__main__":
    run()
