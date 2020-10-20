# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 20                             | #
# | 6616 문자열 암호화                   | #
# -------------------------------------- #


def run():
    while True:
        N = int(r_input())

        if N == 0:
            break
        
        text = r_input().rstrip()
        text = text.replace(' ', '')
        text = text.upper()

        length = len(text)
        res = [-1] * length
        
        ind = 0
        start_ind = 0
        to_ind = 0

        while ind < length:
            res[to_ind] = text[ind]
            
            to_ind += N

            if to_ind >= length:
                start_ind += 1
                to_ind = start_ind

            ind += 1

        print(''.join(res))


if __name__ == "__main__":
    run()
