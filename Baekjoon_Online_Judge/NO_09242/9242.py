# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 13                             | #
# | 9242 폭탄 해체                      | #
# -------------------------------------- #


def run():
    numbers = {'**** ** ** ****': '0', '  *  *  *  *  *': '1', '***  *****  ***': '2', '***  ****  ****': '3', '* ** ****  *  *': '4', '****  ***  ****': '5',
    '****  **** ****': '6', '***  *  *  *  *': '7', '**** ***** ****': '8', '**** ****  ****': '9'}

    bomb = [r_input().rstrip() for _ in range(5)]

    res = ''
    
    for ind in range(0, len(bomb[0]), 4):
        save = ''

        for row in range(5):
            tmp = bomb[row][ind: ind + 3]
            length = len(tmp)

            tmp += ' ' * (3 - length)

            save += tmp
        
        if save not in numbers:
            print('BOOM!!')
            sys.exit()

        res += numbers[save]
    
    if int(res) % 6:
        print('BOOM!!')
    
    else:
        print('BEER!!')


if __name__ == "__main__":
    run()
