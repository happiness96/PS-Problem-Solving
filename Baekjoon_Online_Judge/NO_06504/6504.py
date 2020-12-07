# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 07                             | #
# | 6504 킬로미터를 마일로               | #
# -------------------------------------- #


def run():
    t = int(r_input())

    save = [1, 2]
    for _ in range(19):
        save.append(save[-1] + save[-2])

    for _ in range(t):
        x = int(r_input())
        tmp = ''

        for val in save[::-1]:
            tmp += str(x // val)

            x %= val
        
        tmp = int(tmp[: -1])

        res = 0

        for ind, val in enumerate(str(tmp)[::-1]):
            if val == '1':
                res += save[ind]
        
        print(res)


if __name__ == "__main__":
    run()
