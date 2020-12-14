# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 14                             | #
# | 1924 2007년                        | #
# -------------------------------------- #


if __name__ == "__main__":
    x, y = map(int, r_input().split())

    days = y

    for month in range(1, x):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days += 31
        
        elif month == 2:
            days += 28
        
        else:
            days += 30
    
    print(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][days % 7])