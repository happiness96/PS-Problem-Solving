# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 08                           | #
# | Day 15                             | #
# | 5397 키로거                        | #
# -------------------------------------- #


def run():
    T = int(r_input())

    for _ in range(T):
        log = r_input().rstrip()
        cur_l = []
        cur_r = []

        for ch in log:
            if ch == '<':
                if cur_l:
                    cur_r.append(cur_l.pop())

            elif ch == '>':
                if cur_r:
                    cur_l.append(cur_r.pop())
            
            elif ch == '-':
                if cur_l:
                    cur_l.pop()
            
            else:
                cur_l.append(ch)
        
        print(''.join(cur_l) + ''.join(cur_r[::-1]))


if __name__ == "__main__":
    run()
