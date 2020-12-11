# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 12                           | #
# | Day 11                             | #
# | 4355 숫자 맞추기                    | #
# -------------------------------------- #


if __name__ == "__main__":
    mini = 0
    maxi = 11

    while True:
        number = int(r_input())

        if number == 0:
            break

        answer = r_input().rstrip()

        if answer == 'right on':
            if mini < number < maxi:
                print('Stan may be honest')
            
            else:
                print('Stan is dishonest')
            
            mini = 0
            maxi = 11
        
        elif answer == 'too high':
            maxi = min(maxi, number)
        
        else:
            mini = max(mini, number)
