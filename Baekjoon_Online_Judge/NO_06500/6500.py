# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 29                             | #
# | 6500 랜덤 숫자 만들기               | #
# -------------------------------------- #


def run():
    while True:
        a = int(r_input())
        
        if not a:
            break

        save = set([a])

        while True:
            a =  str(a * a)
            a = '0' * (8 - len(a)) + a

            tmp = int(a[2: 6])

            if tmp in save:
                break

            save.add(tmp)

            a = tmp
        
        print(len(save))


if __name__ == "__main__":
    run()
