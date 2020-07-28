# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# ---------------------------- #
# | Created by happiness96   | #
# | Year 2020                | #
# | Month 07                 | #
# | Day 28                   | #
# | 16769 Mixing Milk        | #
# ---------------------------- #


if __name__ == "__main__":
    c1, m1 = map(int, r_input().split())
    c2, m2 = map(int, r_input().split())
    c3, m3 = map(int, r_input().split())

    for cnt in range(100):
        if cnt % 3 == 0:
            pour = min(c2 - m2, m1)

            m1 -= pour
            m2 += pour
        
        elif cnt % 3 == 1:
            pour = min(c3 - m3, m2)

            m2 -= pour
            m3 += pour
        
        else:
            pour = min(c1 - m1, m3)

            m3 -= pour
            m1 += pour
    
    print(m1)
    print(m2)
    print(m3)
