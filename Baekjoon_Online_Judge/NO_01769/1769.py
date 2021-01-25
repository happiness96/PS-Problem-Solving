# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2021                          | #
# | Month 01                           | #
# | Day 25                             | #
# | 1769 3의 배수                       | #
# -------------------------------------- #


def chk(X, deep):
    if len(X) == 1:
        print(deep)
        
        if int(X) % 3:
            return False
        
        else:
            return True
    
    total = 0

    for x in X:
        total += int(x)
    
    return chk(str(total), deep + 1)


if __name__ == "__main__":
    X = r_input().rstrip()

    if chk(X, 0):
        print('YES')
    
    else:
        print('NO')
