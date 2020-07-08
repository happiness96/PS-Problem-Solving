# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 08                   | #
# | 3061 사다리               | #
# ---------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        N = int(r_input())
        dest = list(map(int, r_input().split()))

        cnt = 0
        save = [0] * (N + 1)

        for num in dest:
            cnt += sum(save[num:])
            save[num] = 1
        
        print(cnt)


if __name__ == "__main__":
    run()
