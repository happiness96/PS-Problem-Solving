# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 10                             | #
# | 20001 고무오리 디버깅               | #
# -------------------------------------- #


if __name__ == "__main__":
    r_input()
    rem_problem = 0

    while True:
        solve = r_input().rstrip()

        if solve == '고무오리 디버깅 끝':
            break
        
        elif solve == '문제':
            rem_problem += 1 
        
        else:
            if rem_problem == 0:
                rem_problem = 2

            else:
                rem_problem -= 1
    
    print('힝구' if rem_problem else '고무오리야 사랑해')