# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 09                           | #
# | Day 30                             | #
# | 17502 클레어와 팰린드롬             | #
# -------------------------------------- #


def run():
    N = int(r_input())

    string = r_input().rstrip()
    rev_string = string[::-1]

    res = ''

    for ind, ch in enumerate(string):
        rev_ch = rev_string[ind]

        if ch == rev_ch == '?':
            res += 'a'
        
        elif ch == '?':
            res += rev_ch
        
        else:
            res += ch
        
    print(res)


if __name__ == "__main__":
    run()
