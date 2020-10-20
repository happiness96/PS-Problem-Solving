# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 7481 ATM놀이                          | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        a, b, S = map(int, r_input().split())

        flag = 0

        if a > b:
            flag = 1
            a, b = b, a
        
        chk = 0
        for money_b in range(S // b * b, -1, -b):
            if (S - money_b) % a == 0:
                if flag:
                    print(money_b // b, (S - money_b) // a)
                    chk = 1
                    break

                else:
                    print((S - money_b) // a, money_b // b)
                    chk = 1
                    break
        
        if not chk:
            print('Impossible')


if __name__ == "__main__":
    run()
