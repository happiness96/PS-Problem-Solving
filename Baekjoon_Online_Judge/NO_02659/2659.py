# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# -------------------------------------- #
# | Created by happiness96             | #
# | Year 2020                          | #
# | Month 10                           | #
# | Day 31                             | #
# | 2659 십자카드 문제                  | #
# -------------------------------------- #


def run():
    cards = ''.join(list(map(str, r_input().rstrip().split())))
    cards += cards

    res = 1

    for number in range(1111, 10000):
        str_num = str(number)
        
        if '0' not in str_num:
            tmp = str_num + str_num

            save = tmp

            for ind in range(4):
                save = min(save, tmp[ind: ind + 4])
            
            if save != str_num:
                continue
            
            if str_num in cards:
                print(res)
                break
            
            res += 1


if __name__ == "__main__":
    run()
